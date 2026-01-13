from __future__ import annotations
import logging
import re
from typing import List, Tuple

from bs4 import BeautifulSoup

from .config import Config
from .http_client import HttpClient
from .url_utils import normalize_url, registrable_domain, is_blocked_domain

log = logging.getLogger(__name__)

def _tokenize_company(name: str) -> list[str]:
    toks = re.findall(r"[a-z0-9]+", (name or "").lower())
    return [t for t in toks if len(t) >= 3]

def score_candidate(url: str, title: str, snippet: str, company_name: str) -> float:
    score = 0.0
    dom = registrable_domain(url) or ""
    toks = _tokenize_company(company_name)
    text = (title + " " + snippet + " " + dom).lower()

    hits = sum(1 for t in toks if t in text)
    score += hits * 2.0

    if url.startswith("https://"):
        score += 0.5

    for t in toks:
        if t in dom:
            score += 1.0
            break

    score -= max(0, len(url) - 30) / 100.0
    return score

async def discover_website(client: HttpClient, cfg: Config, company_name: str, country: str = "", website_hint: str = "") -> List[str]:
    out: List[str] = []

    if website_hint:
        u = normalize_url(website_hint)
        if u and not is_blocked_domain(u, cfg.blocked_domains):
            out.append(u)

    q = f"{company_name} official website"
    if country:
        q += f" {country}"
    q_param = re.sub(r"\s+", "+", q.strip())
    search_url = f"{cfg.ddg_html_url}?q={q_param}"

    html = await client.get_text(search_url)
    if not html:
        return out

    soup = BeautifulSoup(html, "lxml")
    candidates: List[Tuple[float, str]] = []

    for r in soup.select("div.result"):
        a = r.select_one("a.result__a")
        if not a:
            continue
        href = a.get("href") or ""
        url = normalize_url(href)
        if not url:
            continue
        if is_blocked_domain(url, cfg.blocked_domains):
            continue

        title = (a.get_text() or "").strip()
        sn = ""
        sn_el = r.select_one(".result__snippet")
        if sn_el:
            sn = (sn_el.get_text() or "").strip()

        sc = score_candidate(url, title, sn, company_name)
        candidates.append((sc, url))

    candidates.sort(key=lambda t: t[0], reverse=True)

    seen = set()
    for _, url in candidates:
        d = registrable_domain(url)
        if not d or d in seen:
            continue
        seen.add(d)
        out.append(url)
        if len(out) >= cfg.search_results_limit:
            break

    return out

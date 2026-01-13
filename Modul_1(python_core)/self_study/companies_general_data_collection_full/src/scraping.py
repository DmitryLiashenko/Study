from __future__ import annotations
import re
from typing import List, Set, Tuple

from bs4 import BeautifulSoup

from .url_utils import safe_join, same_registrable_domain

EMAIL_RE = re.compile(r"(?i)([a-z0-9._%+-]+)@([a-z0-9.-]+\.[a-z]{2,})")

OBFUSCATED_PATTERNS = [
    (re.compile(r"(?i)([a-z0-9._%+-]+)\s*\[at\]\s*([a-z0-9.-]+)\s*\[dot\]\s*([a-z]{2,})"),
     lambda m: f"{m.group(1)}@{m.group(2)}.{m.group(3)}"),
    (re.compile(r"(?i)([a-z0-9._%+-]+)\s*\(at\)\s*([a-z0-9.-]+)\s*\(dot\)\s*([a-z]{2,})"),
     lambda m: f"{m.group(1)}@{m.group(2)}.{m.group(3)}"),
]

KEYWORDS = ("contact", "about", "support", "impressum", "legal", "privacy", "terms", "company", "team", "press")

def extract_emails(html: str) -> Set[str]:
    emails: Set[str] = set()
    for m in EMAIL_RE.finditer(html):
        emails.add(f"{m.group(1)}@{m.group(2)}".lower())
    for rx, fn in OBFUSCATED_PATTERNS:
        for m in rx.finditer(html):
            emails.add(fn(m).lower())
    return emails

def extract_mailtos(html: str) -> Set[str]:
    emails: Set[str] = set()
    soup = BeautifulSoup(html, "lxml")
    for a in soup.select("a[href^='mailto:']"):
        href = a.get("href") or ""
        addr = href.split("mailto:", 1)[-1].split("?", 1)[0].strip().lower()
        if addr:
            emails.add(addr)
    return emails

def extract_links(base_url: str, html: str) -> List[str]:
    soup = BeautifulSoup(html, "lxml")
    links: List[str] = []
    for a in soup.find_all("a"):
        href = a.get("href") or ""
        if not href:
            continue
        full = safe_join(base_url, href)
        if full and full.startswith("http"):
            links.append(full)

    seen = set()
    out = []
    for u in links:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out

def prioritize_links(base_url: str, links: List[str]) -> List[str]:
    same = [u for u in links if same_registrable_domain(base_url, u)]
    scored: List[Tuple[int, str]] = []
    for u in same:
        lu = u.lower()
        sc = 0
        if any(k in lu for k in KEYWORDS):
            sc += 10
        sc -= lu.count("/")
        scored.append((sc, u))
    scored.sort(key=lambda t: t[0], reverse=True)

    out = []
    seen = set()
    for _, u in scored:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out

def crawl_plan(start_url: str, first_html: str, max_pages: int) -> List[str]:
    links = extract_links(start_url, first_html)
    pri = prioritize_links(start_url, links)

    plan = [start_url]
    for u in pri:
        if u not in plan:
            plan.append(u)
        if len(plan) >= max_pages:
            break
    return plan[:max_pages]

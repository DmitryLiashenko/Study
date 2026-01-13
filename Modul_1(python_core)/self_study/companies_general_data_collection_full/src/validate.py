from __future__ import annotations
import re
from typing import Tuple, Optional

from bs4 import BeautifulSoup
import dns.resolver
from email_validator import validate_email, EmailNotValidError

from .url_utils import registrable_domain

def _tokens(name: str) -> list[str]:
    toks = re.findall(r"[a-z0-9]+", (name or "").lower())
    return [t for t in toks if len(t) >= 3]

def verify_website(html: str, company_name: str, text_limit: int) -> Tuple[bool, str]:
    toks = _tokens(company_name)
    if not toks:
        return False, "No meaningful tokens in company name."

    soup = BeautifulSoup(html, "lxml")

    title = (soup.title.string if soup.title and soup.title.string else "") or ""
    metas = []
    for m in soup.find_all("meta"):
        key = (m.get("name") or m.get("property") or "").lower()
        if key in ("description", "og:site_name", "og:title"):
            metas.append(m.get("content") or "")

    heads = " ".join((h.get_text(" ", strip=True) or "") for h in soup.find_all(["h1", "h2"])[:3])
    footer = ""
    foot = soup.find("footer")
    if foot:
        footer = foot.get_text(" ", strip=True)[:1000]

    visible = soup.get_text(" ", strip=True)[:text_limit]
    sample = (title + " " + " ".join(metas) + " " + heads + " " + footer + " " + visible).lower()

    hits = sum(1 for t in toks if t in sample)
    threshold = 1 if len(toks) <= 2 else 2
    ok = hits >= threshold
    return ok, f"Token hits {hits}/{len(toks)} (threshold={threshold})"

def site_domain(url: str) -> Optional[str]:
    return registrable_domain(url)

def email_domain_matches_site(email: str, site_dom: str) -> bool:
    email_dom = email.split("@")[-1].lower()
    return email_dom == site_dom or email_dom.endswith("." + site_dom)

def verify_email(email: str, site_dom: str, mx_check: bool) -> Tuple[bool, str]:
    try:
        v = validate_email(email, check_deliverability=False)
    except EmailNotValidError as e:
        return False, f"Invalid syntax: {e}"

    if not email_domain_matches_site(email, site_dom):
        return False, f"Domain mismatch (site={site_dom})"

    if mx_check:
        try:
            dns.resolver.resolve(v.domain, "MX")
        except Exception as e:
            return False, f"No MX: {e}"

    return True, "OK"

from __future__ import annotations
import re
from urllib.parse import urlparse, urlunparse
import tldextract
import validators

def normalize_url(url: str) -> str | None:
    url = (url or "").strip()
    if not url:
        return None
    if url.startswith("//"):
        url = "https:" + url
    if not re.match(r"^https?://", url):
        url = "https://" + url

    try:
        p = urlparse(url)
        if p.scheme not in ("http", "https"):
            return None
        p = p._replace(fragment="")
        netloc = (p.netloc or "").lower().replace(":80", "").replace(":443", "")
        p = p._replace(netloc=netloc)
        url = urlunparse(p)
    except Exception:
        return None

    if not validators.url(url):
        return None
    return url

def registrable_domain(url: str) -> str | None:
    try:
        ext = tldextract.extract(url)
        if ext.domain and ext.suffix:
            return f"{ext.domain}.{ext.suffix}".lower()
        return None
    except Exception:
        return None

def is_blocked_domain(url: str, blocked: tuple[str, ...]) -> bool:
    d = registrable_domain(url)
    if not d:
        return True
    return any(d == b or d.endswith("." + b) for b in blocked)

def same_registrable_domain(a: str, b: str) -> bool:
    da = registrable_domain(a)
    db = registrable_domain(b)
    return bool(da and db and da == db)

def safe_join(base: str, href: str) -> str | None:
    from urllib.parse import urljoin
    full = urljoin(base, href)
    return normalize_url(full)

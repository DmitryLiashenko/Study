from __future__ import annotations
import json
import logging
from typing import Set, Optional

from .config import Config
from .http_client import HttpClient
from .models import CompanyResult
from .search import discover_website
from .scraping import extract_emails, extract_mailtos, crawl_plan
from .validate import verify_website, site_domain, verify_email, email_domain_matches_site

log = logging.getLogger(__name__)

ROLE_PREFIXES = ("info@", "contact@", "hello@", "support@", "sales@", "office@", "team@", "press@")

def _pick_best_email(emails: Set[str], site_dom: str) -> Optional[str]:
    filtered = sorted([e for e in emails if email_domain_matches_site(e, site_dom)])
    if not filtered:
        return None
    for pref in ROLE_PREFIXES:
        for e in filtered:
            if e.startswith(pref):
                return e
    return filtered[0]

async def process_company(client: HttpClient, cfg: Config, company_name: str, country: str = "", website_hint: str = "") -> CompanyResult:
    base = CompanyResult(company_name=company_name)

    candidates = await discover_website(client, cfg, company_name, country=country, website_hint=website_hint)
    base.candidate_websites = json.dumps(candidates, ensure_ascii=False)

    if not candidates:
        base.notes = "No website candidates (search blocked/failed)."
        return base

    best_fallback: CompanyResult | None = None

    for cand in candidates:
        html = await client.get_text(cand)
        if not html:
            continue

        dom = site_domain(cand)
        if not dom:
            continue

        ok_site, site_note = verify_website(html, company_name, cfg.validation_text_limit)

        plan = crawl_plan(cand, html, cfg.max_pages)
        emails: Set[str] = set()
        pages_scanned = 0

        emails |= extract_emails(html)
        emails |= extract_mailtos(html)
        pages_scanned += 1

        for url in plan[1:]:
            h = await client.get_text(url)
            if not h:
                continue
            pages_scanned += 1
            emails |= extract_emails(h)
            emails |= extract_mailtos(h)

        chosen = _pick_best_email(emails, dom) if emails else None

        out = CompanyResult(
            company_name=company_name,
            website_url=cand,
            website_verified=ok_site,
            email=chosen or "",
            email_verified=False,
            pages_scanned=pages_scanned,
            candidate_websites=base.candidate_websites,
            emails_found=json.dumps(sorted(emails), ensure_ascii=False),
            notes=f"Website: {site_note}",
        )

        if chosen:
            ok_email, email_note = verify_email(chosen, dom, cfg.enable_mx_check)
            out.email_verified = ok_email
            out.notes += f" | Email: {email_note}"
        else:
            out.notes += " | Email: not found on scanned pages."

        if out.website_verified:
            return out

        if best_fallback is None:
            best_fallback = out

    if best_fallback:
        return best_fallback

    base.notes = "Could not fetch any candidate website."
    return base

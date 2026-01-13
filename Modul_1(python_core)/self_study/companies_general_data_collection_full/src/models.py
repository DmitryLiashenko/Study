from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class CompanyResult:
    company_name: str
    website_url: str = ""
    website_verified: bool = False
    email: str = ""
    email_verified: bool = False
    pages_scanned: int = 0
    candidate_websites: str = ""
    emails_found: str = ""
    notes: str = ""

    def to_row(self) -> dict:
        return asdict(self)

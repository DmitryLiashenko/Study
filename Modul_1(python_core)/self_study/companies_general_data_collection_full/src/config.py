from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    concurrency: int = 20
    timeout_s: int = 25
    max_pages: int = 6
    search_results_limit: int = 8
    per_host_limit: int = 3
    max_retries: int = 2
    enable_mx_check: bool = False

    user_agent: str = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0 Safari/537.36"
    )
    accept_language: str = "en-US,en;q=0.9"
    ddg_html_url: str = "https://duckduckgo.com/html/"
    validation_text_limit: int = 6000

    blocked_domains: tuple[str, ...] = (
        "facebook.com", "instagram.com", "linkedin.com", "twitter.com", "x.com",
        "wikipedia.org", "crunchbase.com", "bloomberg.com", "reuters.com",
        "youtube.com", "medium.com"
    )

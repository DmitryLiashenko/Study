# Companies General Data Collection — Full Test Task Solution

A practical, “full” implementation for the test task: for each company, discover and verify an official website, then collect and validate an email address.

## Features
- **Async** crawling with `asyncio` + `aiohttp`
- **Website discovery** via DuckDuckGo HTML search (no JS) with candidate scoring
- **Website verification** heuristics:
  - company name tokens in `<title>`, meta tags, headers, footer, visible text sample
  - optional “About/Contact” page signals
- **Email extraction**:
  - direct emails in HTML
  - `mailto:` links
  - common obfuscations: `name [at] domain [dot] com`, `name(at)domain.com`
- **Email validation**:
  - syntax validation via `email-validator`
  - domain match to site registrable domain (subdomains allowed)
  - optional **MX check**
- **Same-domain crawling** up to N pages (homepage + prioritized contact/about/legal links + BFS fallback)
- **Reproducible output**: `notes`, `pages_scanned`, `candidate_websites`, `emails_found`

## Project structure
```
companies_general_data_collection_full/
├── src/
│   ├── main.py                 # CLI entrypoint
│   ├── config.py               # config dataclass
│   ├── io_utils.py             # read input, write output
│   ├── logging_utils.py        # logging config
│   ├── http_client.py          # aiohttp wrapper with retries/backoff + per-host limits
│   ├── url_utils.py            # url normalization, domain extraction, filters
│   ├── search.py               # DuckDuckGo HTML search + candidate extraction/scoring
│   ├── scraping.py             # link extraction, email extraction, crawl planning
│   ├── validate.py             # website + email validation
│   ├── pipeline.py             # per-company orchestration
│   └── models.py               # result dataclasses
├── data/
│   └── companies.csv           # example input
├── output/
│   └── results.csv             # generated output
├── requirements.txt
└── run.sh
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Input
`data/companies.csv` must contain `company_name`.
Optional columns:
- `country`
- `website_hint`

Example:
```csv
company_name,country,website_hint
OpenAI,USA,
Deep Knowledge Group,UK,
```

## Run
```bash
python -m src.main --input data/companies.csv --output output/results.csv --concurrency 20 --max-pages 6 --mx-check
```

## Output columns
- `company_name`
- `website_url`
- `website_verified`
- `email`
- `email_verified`
- `pages_scanned`
- `emails_found`
- `candidate_websites`
- `notes`

## Notes
- Website discovery via DuckDuckGo HTML may be rate-limited. If accuracy is critical, supply `website_hint` in input.
- This is a test-task style crawler; production would include stronger entity resolution and more robust search sources.

from __future__ import annotations
import argparse
import asyncio
import logging
import pandas as pd

from .config import Config
from .logging_utils import setup_logging
from .io_utils import read_companies, write_results
from .http_client import HttpClient
from .pipeline import process_company

log = logging.getLogger(__name__)

async def run(input_path: str, output_path: str, cfg: Config) -> None:
    df = read_companies(input_path)
    sem = asyncio.Semaphore(cfg.concurrency)

    async with HttpClient(
        timeout_s=cfg.timeout_s,
        user_agent=cfg.user_agent,
        accept_language=cfg.accept_language,
        max_retries=cfg.max_retries,
        per_host_limit=cfg.per_host_limit,
    ) as client:

        async def one(row) -> dict:
            async with sem:
                r = await process_company(
                    client,
                    cfg,
                    company_name=row["company_name"],
                    country=row.get("country", "") or "",
                    website_hint=row.get("website_hint", "") or "",
                )
                return r.to_row()

        tasks = [one(row) for _, row in df.iterrows()]
        results = await asyncio.gather(*tasks)

    out_df = pd.DataFrame(results)
    write_results(out_df, output_path)
    log.info("Saved: %s (rows=%d)", output_path, len(out_df))

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--concurrency", type=int, default=20)
    p.add_argument("--timeout", type=int, default=25)
    p.add_argument("--max-pages", type=int, default=6)
    p.add_argument("--mx-check", action="store_true")
    p.add_argument("--log-level", default="INFO", choices=["DEBUG","INFO","WARNING","ERROR"])
    return p.parse_args()

def main():
    args = parse_args()
    setup_logging(args.log_level)

    cfg = Config(
        concurrency=args.concurrency,
        timeout_s=args.timeout,
        max_pages=args.max_pages,
        enable_mx_check=args.mx_check,
    )
    asyncio.run(run(args.input, args.output, cfg))

if __name__ == "__main__":
    main()

from __future__ import annotations
import asyncio
import logging
from collections import defaultdict
from typing import Optional
from urllib.parse import urlparse

import aiohttp

log = logging.getLogger(__name__)

class HttpClient:
    def __init__(
        self,
        *,
        timeout_s: int,
        user_agent: str,
        accept_language: str,
        max_retries: int,
        per_host_limit: int,
    ):
        self._timeout = aiohttp.ClientTimeout(total=timeout_s)
        self._headers = {
            "User-Agent": user_agent,
            "Accept-Language": accept_language,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
        self._max_retries = max_retries
        self._session: Optional[aiohttp.ClientSession] = None
        self._per_host = defaultdict(lambda: asyncio.Semaphore(per_host_limit))

    async def __aenter__(self) -> "HttpClient":
        self._session = aiohttp.ClientSession(timeout=self._timeout, headers=self._headers)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._session:
            await self._session.close()

    async def get_text(self, url: str) -> Optional[str]:
        assert self._session is not None
        host = (urlparse(url).netloc or "").lower()
        sem = self._per_host[host]

        last_err = None
        for attempt in range(self._max_retries + 1):
            try:
                async with sem:
                    async with self._session.get(url, allow_redirects=True) as resp:
                        if resp.status >= 400:
                            return None
                        return await resp.text(errors="ignore")
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                last_err = e
                await asyncio.sleep(0.6 * (attempt + 1))
        if last_err:
            log.debug("GET failed %s: %r", url, last_err)
        return None

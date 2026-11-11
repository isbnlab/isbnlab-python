"""Offline test helpers: a fake urllib3 pool that answers from tests/fixtures."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Optional
from urllib.parse import urlsplit

import pytest
import urllib3

import isbnlab

FIXTURES = Path(__file__).parent / "fixtures"


class FakePool:
    """Stands in for urllib3.PoolManager: records each request, returns one canned response."""

    def __init__(self, status: int, body: bytes, headers: Optional[dict] = None) -> None:
        self.status = status
        self.body = body
        self.headers = headers or {}
        self.requests: list = []

    def request(self, method: str, url: str, **kwargs: Any) -> urllib3.HTTPResponse:
        self.requests.append({"method": method, "url": url, **kwargs})
        return urllib3.HTTPResponse(
            body=self.body,
            status=self.status,
            headers={"Content-Type": "application/json", **self.headers},
            preload_content=True,
        )

    @property
    def last(self) -> dict:
        return self.requests[-1]

    @property
    def last_path(self) -> str:
        return urlsplit(self.last["url"]).path

    @property
    def last_query(self) -> str:
        return urlsplit(self.last["url"]).query


@pytest.fixture
def respond() -> Callable[..., tuple]:
    """respond("book.json") or respond(status=404, body={...}) -> (ApiClient, FakePool)."""

    def make(fixture: Optional[str] = None, status: int = 200, body: Any = None, headers: Optional[dict] = None):
        data = (FIXTURES / fixture).read_bytes() if fixture else json.dumps(body).encode()
        config = isbnlab.Configuration(access_token="test-token")
        client = isbnlab.ApiClient(config)
        pool = FakePool(status, data, headers)
        client.rest_client.pool_manager = pool
        return client, pool

    return make

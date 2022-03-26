from typing import Optional
import requests
from requests import Response
from src.sentry_tracing_client import SentryTracing

class RequestHandler(SentryTracing):
    headers: "dict[str, Optional[str]]" = {}

    def prepare(self) -> None:
        self.headers["sentry-trace"] = self.start_trace()

    def make_request(self) -> Response:
        response = requests.get("<upstream_url>", headers=self.headers)
        return response

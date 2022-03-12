import requests
from sentry_tracing_client import SentryTracing

class RequestHandler(SentryTracing):
    headers = None

    def prepare(self):
        self.headers["sentry-trace"] = self.start_trace()

    def make_request(self):
        response = requests.get("<upstream_url>", headers=self.headers)
        return response

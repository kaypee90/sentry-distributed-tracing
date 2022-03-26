class SentryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        sentry_trace = request.META.get("HTTP_SENTRY_TRACE")
        if sentry_trace:
            import sentry_sdk
            trace_id = sentry_trace.split("-")[0]
            transaction = sentry_sdk.Hub.current.scope.transaction
            if transaction:       
                transaction.trace_id = trace_id
        return self.get_response(request)
"""
Author Kaypee90
"""

from typing import Union
import sentry_sdk
import uuid

class SentryTracing:
    sentry_trace = None
    
    def start_trace(self) -> Union[str, None]:
        trace_id = uuid.uuid4().hex
        self.sentry_trace =  trace_id + "-" + uuid.uuid4().hex[16:]

        transaction = sentry_sdk.Hub.current.scope.transaction
        if transaction:
            transaction.trace_id=trace_id
            return self.sentry_trace
            
        return None

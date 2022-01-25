import json
import time
from datetime import datetime, timedelta


class TimeUtilities:

    @staticmethod
    def current_time_in_milliseconds() -> int:
        return int(time.time() * 1000)

    @staticmethod
    def get_past_time_from_now(hours):
        return datetime.now() - timedelta(hours=hours)


class RequestUtilities:

    @staticmethod
    def load_request_body(request) -> dict:

        try:
            request_body = json.loads(request.body)

        except Exception as e:
            print(e.args)
            request_body = {}

        return request_body

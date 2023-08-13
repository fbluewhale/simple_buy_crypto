import socket
import time
import json
import logging
from rest_framework.exceptions import APIException

request_logger = logging.getLogger("incoming")
error_logger = logging.getLogger("django")


class RequestLogMiddleware:
    """Request Logging Middleware."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        log_data = {
            "remote_address": request.META["REMOTE_ADDR"],
            "request_method": request.method,
            "request_path": request.get_full_path(),
        }

        if "/api/" in str(request.get_full_path()):
            req_body = json.loads(request.body.decode("utf-8")) if request.body else {}
            log_data["request_body"] = req_body

        response = self.get_response(request)
        try:
            if response and "application/json" in response["content-type"]:
                response_body = json.loads(response.content.decode("utf-8"))
                log_data["response_body"] = response_body
            log_data["duration"] = time.time() - start_time

            request_logger.info(msg=log_data)
            return response
        except:
            error_logger.error(msg=log_data)
            return response

    def process_exception(self, request, exception):
        try:
            raise exception
        except Exception as e:
            error_logger.exception("Unhandled Exception: " + str(e))
        return exception

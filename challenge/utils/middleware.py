import time
import json
import logging
from urllib.parse import unquote
from rest_framework.exceptions import APIException
from rest_framework import status

request_logger = logging.getLogger("incoming")
app_logger = logging.getLogger("app")
error_logger = logging.getLogger("error")


class RequestLogMiddleware:
    """Request Logging Middleware."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.api_prefix = "/api/"

    def __call__(self, request):
        start_time = time.time()
        log_data = {
            "remote_address": request.META["REMOTE_ADDR"],
            "request_method": request.method,
            "request_path": request.get_full_path(),
        }

        if self.api_prefix in str(request.get_full_path()):
            if request.body:
                req_body = request.body
                req_body = str(req_body, encoding="utf-8")
                req_body = unquote(req_body)
                req_body = json.loads(req_body)
            else:
                req_body = {}
            log_data["request_body"] = req_body

        response = self.get_response(request)
        try:
            if response and "application/json" in response["content-type"]:
                if request.body:
                    response_body = response.content.decode("utf-8")
                    response_body = unquote(response_body)
                    response_body = json.loads(response_body)
                else:
                    response_body = {}
                log_data["response_body"] = response_body
            log_data["duration"] = time.time() - start_time
            if response.status_code >= status.HTTP_400_BAD_REQUEST:
                app_logger.info(msg=json.dumps(log_data))
            else:
                request_logger.info(msg=json.dumps(log_data))
            return response
        except:
            error_logger.error(msg=json.dumps(log_data))
            return response

    def process_exception(self, request, exception):
        try:
            raise exception
        except Exception as e:
            error_logger.exception("Unhandled Exception: " + str(e))
        return exception

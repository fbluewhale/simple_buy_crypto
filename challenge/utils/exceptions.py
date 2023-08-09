from rest_framework.exceptions import APIException, _get_error_details
from rest_framework import status


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Service temporarily unavailable, try again later."

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        self.detail = _get_error_details(detail, code)


class ValidationException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Service temporarily unavailable, try again later."

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        self.detail = _get_error_details(detail, code)

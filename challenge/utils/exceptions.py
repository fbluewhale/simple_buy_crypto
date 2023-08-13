from rest_framework.exceptions import APIException, _get_error_details
from rest_framework import status


class BaseException(APIException):
    status_code = None
    default_detail = None

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        self.detail = _get_error_details(detail, code)


class BadRequest(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Bad Request"


class ValidationException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "validation Error"


class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "not found"

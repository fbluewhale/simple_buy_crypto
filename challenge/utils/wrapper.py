from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json, serializer_helpers


class JSONResponseWrapper(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status = (
            "success" if renderer_context["response"].status_code < 400 else "failure"
        )
        if data and not type(data) in [
            "",
            None,
            type(list()),
            serializer_helpers.ReturnDict,
        ]:
            count = data.pop("count", None)
            next = data.pop("next", None)
            previous = data.pop("previous", None)
            error_message = ""
        else:
            data, temp = dict(), data
            count = 0
            next = None
            previous = None
            error_message = ""
            data["result"] = temp

        response = {
            "status": status,
            "count": count,
            "next": next,
            "previous": previous,
            "error_message": error_message,
            **data,
        }

        return super(JSONResponseWrapper, self).render(
            response, accepted_media_type, renderer_context
        )

import json
import logging

from werkzeug.exceptions import BadRequest, InternalServerError, NotFound

log = logging.getLogger(__name__)


#
# HTTP overloads
#
class ApiInternalError(InternalServerError):
    """*500* `Internal Server Error`"""

    def __init__(self, **kwargs):
        self.subcode = kwargs.pop("subcode", 0)
        InternalServerError.__init__(self, **kwargs)


class ApiNotFound(NotFound):
    """*404* `NotFound`"""

    def __init__(self, **kwargs):
        self.subcode = kwargs.pop("subcode", 0)
        NotFound.__init__(self, **kwargs)


class ApiBadRequest(BadRequest):
    """*400* `BadRequest`"""

    def __init__(self, **kwargs):
        self.subcode = kwargs.pop("subcode", 0)
        self.errors = kwargs.pop("errors", 0)
        if type(self.errors) == list:
            kwargs["description"] = ";\n".join(self.errors)
        elif type(self.errors) == dict:
            kwargs["description"] = json.dumps(self.errors)

        BadRequest.__init__(self, **kwargs)


#
# internal exceptions
#
class ApiValidationError(ApiBadRequest):
    """*400* `BadRequest`"""


class DataServiceException(Exception):
    ...

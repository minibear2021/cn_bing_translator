from enum import Enum, unique


@unique
class RequestType(Enum):
    GET = 'GET'
    POST = 'POST'
    PATCH = 'PATCH'
    PUT = 'PUT'
    DELETE = 'DELETE'

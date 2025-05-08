from functools import wraps
from uuid import uuid4

from flask import g, request


def generate_request_id():
    """Generate a unique request ID or use the one from incoming request header"""
    request_id = request.headers.get("X-Request-ID")
    if not request_id:
        request_id = str(uuid4())
    return request_id


def request_context_middleware():
    def middleware(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            g.request_id = generate_request_id()
            return f(*args, **kwargs)

        return decorated

    return middleware

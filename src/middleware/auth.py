from functools import wraps
from http import HTTPStatus

import jwt
from flask import g, jsonify, request

from ..config.settings import settings
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def validate_token():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None

            # Get token from Authorization header
            if "Authorization" in request.headers:
                auth_header = request.headers["Authorization"]
                try:
                    token = auth_header.split(" ")[1]  # Split 'Bearer <token>'
                except IndexError:
                    logger.error("Invalid Authorization header format")
                    return (
                        jsonify({"message": "Invalid token format"}),
                        HTTPStatus.UNAUTHORIZED,
                    )

            if not token:
                logger.error("No token provided")
                return jsonify({"message": "Token is missing"}), HTTPStatus.UNAUTHORIZED

            try:
                # Decode token
                payload = jwt.decode(token, settings.jwt_secret_key, algorithms=["HS256"])

                # Store the entire payload in g.user
                g.user = payload

                # Validate required claims
                if "user_id" not in payload:
                    logger.error("Token missing required claim: user_id")
                    return (
                        jsonify({"message": "Invalid token"}),
                        HTTPStatus.UNAUTHORIZED,
                    )

                if "role" not in payload:
                    logger.error("Token missing required claim: role")
                    return (
                        jsonify({"message": "Invalid token"}),
                        HTTPStatus.UNAUTHORIZED,
                    )

            except jwt.ExpiredSignatureError:
                logger.error("Token has expired")
                return (
                    jsonify({"message": "Token has expired"}),
                    HTTPStatus.UNAUTHORIZED,
                )
            except jwt.InvalidTokenError as e:
                logger.error(f"Invalid token: {str(e)}")
                return jsonify({"message": "Invalid token"}), HTTPStatus.UNAUTHORIZED

            return f(*args, **kwargs)

        return decorated_function

    return decorator

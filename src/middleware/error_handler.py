"""Error handling middleware for Flask applications"""

from functools import wraps
from http import HTTPStatus
from typing import Any, Callable

from flask import current_app
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from ..utils.exceptions import DatabaseError, ResourceNotFoundError, ServiceError
from ..utils.response_builder import ResponseBuilder


def handle_request_errors(f: Callable) -> Callable:
    """Decorator to handle common API errors and return consistent responses"""

    @wraps(f)
    def decorated(*args: Any, **kwargs: Any) -> Any:
        try:
            return f(*args, **kwargs)

        except BadRequest as err:
            current_app.logger.error(f"Invalid JSON request: {str(err)}", exc_info=True)
            return ResponseBuilder.error(message=str(err), status_code=HTTPStatus.BAD_REQUEST)

        except ValidationError as err:
            current_app.logger.error(f"Validation failed: {str(err)}", exc_info=True)
            return ResponseBuilder.error(
                message="Validation failed",
                errors=err.messages,
                status_code=HTTPStatus.BAD_REQUEST,
            )

        except ResourceNotFoundError as err:
            current_app.logger.error(f"Resource not found: {str(err)}", exc_info=True)
            return ResponseBuilder.error(
                message=str(err),
                status_code=HTTPStatus.NOT_FOUND,
            )

        except (ServiceError, DatabaseError) as err:
            current_app.logger.error(f"Service error: {str(err)}", exc_info=True)
            return ResponseBuilder.error(
                message=str(err),
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

        except Exception as err:
            current_app.logger.error(f"Unexpected error in request: {str(err)}", exc_info=True)
            return ResponseBuilder.error(
                message="Internal server error",
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    return decorated

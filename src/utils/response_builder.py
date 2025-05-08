from typing import Any, Dict, List, Optional

from flask import g, jsonify


class ResponseBuilder:
    """Utility class for building consistent API responses"""

    @staticmethod
    def success(
        data: Optional[Any] = None,
        message: Optional[str] = None,
        status_code: int = 200,
    ) -> tuple:
        """Build success response"""
        response = {
            "status": "success",
            "requestId": getattr(g, "request_id", ""),
        }
        if data is not None:
            response["data"] = data
        if message:
            response["message"] = message
        return jsonify(response), status_code

    @staticmethod
    def error(
        message: str,
        errors: Optional[Dict[str, List[str]]] = None,
        status_code: int = 400,
    ) -> tuple:
        """Build error response"""
        response = {
            "status": "error",
            "requestId": getattr(g, "request_id", ""),
            "message": message,
        }
        if errors:
            response["errors"] = errors
        return jsonify(response), status_code

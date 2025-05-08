from http import HTTPStatus
from flask import Blueprint, request, jsonify
from ..services.user_service import UserService
from ..schemas.user import UserSchema
from ..utils.response_builder import ResponseBuilder
from ..middleware.auth import validate_token
from ..middleware.error_handler import handle_request_errors

user_bp = Blueprint("users", __name__, url_prefix="/api/users")

userService=UserService()
@user_bp.route("/", methods=["POST"])
@handle_request_errors
def create_users():
    users_schema = UserSchema()
    validated_users = users_schema.load(request.json)

    users = userService.create_users(validated_users)
    return ResponseBuilder.success(data=users.to_dict(),status_code=HTTPStatus.CREATED)


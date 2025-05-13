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

# @user_bp.route("/", methods=["GET"])
# def get_users():
#     users = UserService.get_all_users()
#     return users.jsonify(users), 200

@user_bp.route("/", methods=["GET"])
def get_users():
    users= userService.get_all_users()
    user_dicts = [user.__dict__ for user in users]
    return ResponseBuilder.success(data=user_dicts,status_code=HTTPStatus.OK)
@user_bp.route("/<int:user_id>", methods=["GET"])
@handle_request_errors
def get_user_by_id(user_id):
    user = userService.get_user_by_id(user_id)
    if not user:
        return ResponseBuilder.error(message="User not found.",status_code=HTTPStatus.NOT_FOUND)
    return ResponseBuilder.success(data=user.to_dict(),status_code=HTTPStatus.OK)
    
# @user_bp.route("/<int:user_id>", methods=["GET"])
# def get_user_by_id(user_id):
#     user = UserService.get_user_by_id(user_id)
#     if not user:
#         return jsonify({"message": "User not found."}), 404
#     return 


# @user_bp.route("/<int:user_id>", methods=["PUT"])
# def update_user(user_id):
#     json_data = request.get_json()
#     try:
#         user_data = user_schema.load(json_data, partial=True)
#         updated_user = UserService.update_user(user_id, user_data)
#         if not updated_user:
#             return jsonify({"message": "User not found."}), 404
#         return user_schema.jsonify(updated_user), 200
#     except Exception as e:
#         return jsonify({"message": str(e)}), 400


# @user_bp.route("/<int:user_id>", methods=["DELETE"])
# def delete_user(user_id):
#     success = UserService.delete_user(user_id)
#     if not success:
#         return jsonify({"message": "User not found."}), 404
#     return '', 204


# @user_bp.route("/<int:user_id>/profile", methods=["GET"])
# def get_user_profile(user_id):
#     user = UserService.get_user_by_id(user_id)
#     if not user or not user.profile:
#         return jsonify({"message": "User profile not found."}), 404
#     return user_schema.jsonify(user), 200


# @user_bp.route("/<int:user_id>/profile", methods=["PUT"])
# def update_user_profile(user_id):
#     json_data = request.get_json()
#     try:
#         profile_data = user_schema.load(json_data, partial=True)
#         updated_profile = UserService.update_user_profile(user_id, profile_data)
#         if not updated_profile:
#             return jsonify({"message": "User profile not found."}), 404
#         return user_schema.jsonify(updated_profile), 200
#     except Exception as e:
#         return jsonify({"message": str(e)}), 400

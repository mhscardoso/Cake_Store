from flask import Blueprint
from app.user.controller import UserG, UserId

user_api = Blueprint("user_api", __name__)

user_api.add_url_rule("/user", view_func=UserG.as_view("user_geral"), methods=["POST", "GET"])
user_api.add_url_rule("/user/<int:id>", view_func=UserId.as_view("user_ids"), methods=["GET", "PUT", "PATCH", "DELETE"])
from ..user_controller import *
from flask import Blueprint

api.add_resource(Register, "/register/")
api.add_resource(Login, "/login/")
api.add_resource(Profile, "/profile/")

user_blueprint = Blueprint("users", "users", url_prefix="/user")
api.init_app(user_blueprint)

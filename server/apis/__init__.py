from flask import Blueprint
from .user_controller import api as user_api

api_blueprint = Blueprint("apis", "iHello", url_prefix="/v1")
user_api.init_app(api_blueprint)

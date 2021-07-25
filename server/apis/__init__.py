from flask import Blueprint
from .routes.user import user_blueprint

api_blueprint = Blueprint("apis", "iHello", url_prefix="/v1")

api_blueprint.register_blueprint(user_blueprint)

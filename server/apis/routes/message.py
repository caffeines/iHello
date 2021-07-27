from flask import Blueprint
from ..message_controller import *

message_api.add_resource(Messages, "/")

message_blueprint = Blueprint("message", "message", url_prefix="/message")
message_api.init_app(message_blueprint)

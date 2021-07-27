from flask import Blueprint
from ..contacts_controller import *

contacts_api.add_resource(Create, "/")

contact_blueprint = Blueprint("contacts", "contacts", url_prefix="/contact")
contacts_api.init_app(contact_blueprint)

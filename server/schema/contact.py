from flask_marshmallow import Marshmallow
from ..wsgi import App

app = App().get_app()
ma = Marshmallow(app)


class ContactSchema(ma.Schema):
    class Meta:
        fields = ("name", "contact", "created_at", "id", "user_id")


contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)

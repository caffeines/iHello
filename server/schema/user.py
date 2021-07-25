from flask_marshmallow import Marshmallow
from ..wsgi import App

app = App().get_app()
ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("name", "username", "created_at", "id")


user_schema = UserSchema()
users_schema = UserSchema(many=True)

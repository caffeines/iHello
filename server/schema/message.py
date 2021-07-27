from flask_marshmallow import Marshmallow
from ..wsgi import App

app = App().get_app()
ma = Marshmallow(app)


class MessageSchema(ma.Schema):
    class Meta:
        fields = (
            "sender_id",
            "recipient_id",
            "created_at",
            "id",
            "message",
            "seen_at",
            "delivered_at",
        )


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)

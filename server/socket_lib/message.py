from flask_socketio import send, join_room
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlalchemy.exc
from ..data import user
from ..socket_lib import socketio
import server.data.message as message_dao


@socketio.on("connect")
@jwt_required()
def connect(x):
    user_id = get_jwt_identity()
    try:
        user_data = user.get_by_id(user_id=user_id)
        print(f"{user_data.name} connected")
        join_room(user_id)
    except sqlalchemy.exc.SQLAlchemyError as e:
        return {"ok": False}


@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected")


@socketio.on("message")
@jwt_required()
def handle_message(msg):
    try:
        user_id = get_jwt_identity()
        recipient = user.get_by_username(msg["recipient"])
        if recipient is None:
            return dict(code=404, error="User not registered")
        new_message = message_dao.create(
            sender_id=user_id, recipient_id=recipient.id, message=msg["message"]
        )
        response = {
            "user_id": new_message.sender_id.__str__(),
            "recipient_id": new_message.recipient_id.__str__(),
            "message": new_message.message,
            "created_at": new_message.created_at.__str__(),
        }
        return dict(code=200, data=response)
    except TypeError as e:
        print(e)
        return dict(code=400, error="Invalid message request data")
    except sqlalchemy.exc.SQLAlchemyError as e:
        return dict(code=500, error="Database query failed")
    except Exception as e:
        print(e)
        return dict(code=500, error="Something went wrong")

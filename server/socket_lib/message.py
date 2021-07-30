from flask_socketio import send, join_room
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlalchemy.exc
from ..data import user
from ..data import contact
from ..socket_lib import socketio
from ..data import message


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


@socketio.on("deliver_message")
@jwt_required()
def deliver_message(data) -> dict:
    print("message was received: ", data)
    try:
        message_id = data["message_id"]
        recipient_id = get_jwt_identity()
        delivered = message.set_delivered_at(message_id, recipient_id)
        return dict(code=200, data=delivered)
    except TypeError as e:
        print(e)
        return dict(code=400, error="Invalid message request data")
    except sqlalchemy.exc.SQLAlchemyError as e:
        return dict(code=500, error="Database query failed")
    except Exception as e:
        print(e)
        return dict(code=500, error="Something went wrong")


@socketio.on("message")
@jwt_required()
def handle_message(msg):
    try:
        user_id = get_jwt_identity()
        recipient = user.get_by_username(msg["recipient"])
        if recipient is None:
            return dict(code=404, error="User not registered")
        is_exist = contact.get_by_contact(contact=recipient.username, user_id=user_id)
        if is_exist is None:
            return dict(code=422, error="Recipient is not in your contact")
        new_message = message.create(
            sender_id=user_id, recipient_id=recipient.id, message=msg["message"]
        )
        response = {
            "id": new_message.id.__str__(),
            "user_id": new_message.sender_id.__str__(),
            "recipient_id": new_message.recipient_id.__str__(),
            "message": new_message.message,
            "created_at": new_message.created_at.__str__(),
        }
        send(response, to=new_message.recipient_id.__str__())
        return dict(code=200, data=response)
    except TypeError as e:
        print(e)
        return dict(code=400, error="Invalid message request data")
    except sqlalchemy.exc.SQLAlchemyError as e:
        print(e)
        return dict(code=500, error="Database query failed")
    except Exception as e:
        print(e)
        return dict(code=500, error="Something went wrong")

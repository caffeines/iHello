import uuid
import sqlalchemy.exc
from ..database.models import Message
from ..database.client import db
from sqlalchemy import or_


def create(sender_id: str, recipient_id: str, message: str):
    try:
        new_message = Message(
            id=uuid.uuid4(),
            sender_id=uuid.UUID(sender_id),
            message=message,
            recipient_id=recipient_id,
        )
        db.session.add(new_message)
        db.session.commit()
        return new_message
    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        raise e


def get_by_user_id(user_id: str):
    try:
        messages = (
            db.session.query(Message)
            .filter(or_(Message.recipient_id == user_id, Message.sender_id == user_id))
            .all()
        )
        db.session.commit()
        return messages
    except sqlalchemy.exc.SQLAlchemyError as e:
        raise e

import uuid
import sqlalchemy.exc
from ..database.models import Contact
from ..database.client import db


def create(contact: str, user_id: str, name=""):
    try:
        new_contact = Contact(
            contact=contact,
            name=name,
            id=uuid.uuid4(),
            user_id=uuid.UUID(user_id),
        )
        db.session.add(new_contact)
        db.session.commit()
        return new_contact
    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        raise e


def get_by_user_id(user_id: str):
    try:
        contacts = Contact.query.filter_by(user_id=user_id, is_deleted=False).all()
        return contacts
    except sqlalchemy.exc.SQLAlchemyError as e:
        return e

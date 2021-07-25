import uuid
import sqlalchemy.exc
from ..utils.password import hash_password
from ..database.models import User
from ..database.client import db


def create(username: str, name: str, password: str):
    try:
        new_user = User(
            id=uuid.uuid4(),
            username=username,
            name=name,
            password=hash_password(password),
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        raise e


def get_by_username(username: str):
    try:
        user = User.query.filter_by(username=username).first()
        return user
    except sqlalchemy.exc.SQLAlchemyError as e:
        raise e

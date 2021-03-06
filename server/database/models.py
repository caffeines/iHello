from .client import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

CONTACT_LEN = 20


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    username = db.Column(db.String(CONTACT_LEN), unique=True, nullable=False)
    name = db.Column(db.String(70), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contacts = db.relationship("Contact", backref="user", lazy=True)

    def __repr__(self):
        return f"User(username: {self.username}, name: {self.name}, id: {self.id})"


class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    sender_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False)
    recipient_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False
    )
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seen_at = db.Column(db.DateTime, nullable=True)
    delivered_at = db.Column(db.DateTime, nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return (
            f"Message(sender_id: {self.sender_id}, recipient_id: {self.recipient_id}, message: {self.message}, "
            f"is_deleted: {self.is_deleted}, seen_at: {self.seen_at})"
        )


class Contact(db.Model):
    __tablename__ = "contact"
    __table_args__ = (db.UniqueConstraint("user_id", "contact", name="unique_contact"),)
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False)
    contact = db.Column(db.String(CONTACT_LEN), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Contacts(user_id: {self.user_id}, contact: {self.contact}, is_deleted: {self.is_deleted})"

import sqlalchemy.exc
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, Api
from ..data import message
from ..schema.message import messages_schema

message_api = Api()


class Messages(Resource):
    @jwt_required()
    def get(self):
        try:
            user_id = get_jwt_identity()
            messages = message.get_by_user_id(user_id)
            print(messages)
            return messages_schema.dump(messages)
        except sqlalchemy.exc.SQLAlchemyError as e:
            print(e)
            return {"message": "Something went wrong"}, 500
        except Exception as e:
            return {"message": "Something went wrong"}, 500

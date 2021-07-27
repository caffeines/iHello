import sqlalchemy.exc
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, Api, reqparse
from ..data import message
from ..schema.message import messages_schema

message_api = Api()

message_parser = reqparse.RequestParser()
message_parser.add_argument("page", type=int, help="Page cannot be converted")


class Messages(Resource):
    @jwt_required()
    def get(self):
        try:
            args = message_parser.parse_args()
            user_id = get_jwt_identity()
            messages = message.get_by_user_id(user_id, args["page"])
            return messages_schema.dump(messages)
        except sqlalchemy.exc.SQLAlchemyError as e:
            print(e)
            return {"message": "Something went wrong"}, 500
        except Exception as e:
            print(e)
            return {"message": "Something went wrong"}, 500

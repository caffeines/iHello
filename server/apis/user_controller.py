import sqlalchemy.exc
from ..utils.jwt_helper import create_jwt
from flask_restful import Resource, Api, reqparse
from ..data import user as user_data
from ..utils.password import check_password
from ..schema.user import user_schema, users_schema
from ..utils import validator
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Api()

register_parser = reqparse.RequestParser()
register_parser.add_argument(
    "username",
    required=True,
    type=validator.str_min_length(3, "username"),
    location="body",
)
register_parser.add_argument(
    "name", required=True, type=validator.str_min_length(3, "name"), location="body"
)
register_parser.add_argument(
    "password",
    required=True,
    type=validator.str_min_length(6, "password"),
    location="body",
)

login_parser = reqparse.RequestParser()
login_parser.add_argument(
    "username",
    required=True,
    type=validator.str_min_length(3, "username"),
)
login_parser.add_argument(
    "password", required=True, type=validator.str_min_length(6, "password")
)


class Register(Resource):
    def post(self):
        try:
            args = register_parser.parse_args()
            new_user = user_data.create(
                username=args["username"], name=args["name"], password=args["password"]
            )
            return user_schema.jsonify(new_user)

        except sqlalchemy.exc.IntegrityError as e:
            return {"message": "User already exist"}, 409
        except sqlalchemy.exc.SQLAlchemyError as e:
            return {"message": "Something went wrong"}, 500


class Login(Resource):
    def post(self):
        args = login_parser.parse_args()
        try:
            user = user_data.get_by_username(args["username"])
            if user is None:
                return {"message": "User is not registered"}, 404

            matched = check_password(args["password"], user.password)
            if not matched:
                return {"message": "Username or password is incorrect"}, 401

            token = create_jwt(user_id=user.id)
            return {"token": token, "user_type": "public"}, 200

        except sqlalchemy.exc.SQLAlchemyError as e:
            return {"message": "Something went wrong"}, 500


class Profile(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = user_data.get_by_id(user_id)
        return user_schema.jsonify(user)

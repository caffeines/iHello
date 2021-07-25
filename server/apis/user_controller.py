import sqlalchemy.exc
from flask_restful import Resource, Api, reqparse
from ..data import user as user_data
from ..utils.password import check_password
from ..schema.user import user_schema, users_schema

api = Api()

register_parser = reqparse.RequestParser()
register_parser.add_argument(
    "username", required=True, type=str, help="Username can not be empty"
)
register_parser.add_argument(
    "name", required=True, type=str, help="Name can not be empty"
)
register_parser.add_argument(
    "password", required=True, type=str, help="Password can not be empty"
)

login_parser = reqparse.RequestParser()
login_parser.add_argument(
    "username", required=True, type=str, help="Username can not be empty"
)
login_parser.add_argument(
    "password", required=True, type=str, help="Password can not be empty"
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
            return {"message": "Login successful"}, 200

        except sqlalchemy.exc.SQLAlchemyError as e:
            return {"message": "Something went wrong"}, 500


class Profile(Resource):
    def get(self):
        user = user_data.get_by_username("sadat")
        return user


api.add_resource(Register, "/user/register/")
api.add_resource(Login, "/user/login/")
api.add_resource(Profile, "/user/profile/<username>/")

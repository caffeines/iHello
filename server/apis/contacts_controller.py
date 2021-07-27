import sqlalchemy.exc
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, Api, reqparse
from ..utils.validator import str_min_length
from ..data import contact
from ..schema.contact import contact_schema

contacts_api = Api()

create_parser = reqparse.RequestParser()
create_parser.add_argument("contact", type=str_min_length(13, "contact"), required=True)
create_parser.add_argument("name", type=str_min_length(3, "name"), required=False)


class Create(Resource):
    @jwt_required()
    def post(self):
        try:
            args = create_parser.parse_args()
            user_id = get_jwt_identity()
            new_contact = contact.create(
                user_id=user_id, contact=args["contact"], name=args["name"]
            )
            return contact_schema.jsonify(new_contact)
        except sqlalchemy.exc.IntegrityError as e:
            return {"message": "Contact already added"}, 200
        except sqlalchemy.exc.SQLAlchemyError as e:
            print(e)
            return {"message": "Something went wrong"}, 500

    @jwt_required()
    def get(self):
        try:
            user_id = get_jwt_identity()
        except sqlalchemy.exc.SQLAlchemyError:
            return {"message": "Something went wrong"}, 500

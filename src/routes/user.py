from flask import request
from flask_restful import Resource

from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from src.models.user import User
from marshmallow import ValidationError


class UserRoutes(Resource):
    def post(self):
        data = request.get_json()

        if User.query.filter_by(email=data['email']).first() is not None:
            return {'message': 'User already exists'}, HTTP_400_BAD_REQUEST

        user_schema = User.get_schema()
        try:
            # user schema returns a dictionary object
            user = User(**user_schema.load(data))
            # ** is used to unpack the dictionary object
        except ValidationError as err:
            return err.messages, HTTP_400_BAD_REQUEST

        user.create()

        return user_schema.dump(user), HTTP_201_CREATED


class UserList(Resource):
    def get(self):
        return {'message': 'List of users'}, HTTP_200_OK

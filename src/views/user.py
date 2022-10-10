from email import message
from pprint import pprint
from flask import request

from flask_restful import Resource

from src.constants.http_status_codes import *
from src.constants.user_messages import *
from src.models.user import User
from marshmallow import ValidationError


class UserViews(Resource):

    def get(self, user_id):
        """ Get a user by id """
        user = User.query.filter_by(
            _id=user_id).first_or_404(description=USER_NOT_FOUND)

        user_schema = User.get_schema(
            {'name', 'email', 'city', 'state', 'zipcode', 'balance'}
        )
        return user_schema.dump(user), HTTP_200_OK

    def post(self):
        """ Create a new user """
        request_data = request.get_json()

        if User.query.filter_by(email=request_data['email']).first() is not None:
            return USER_ALREADY_EXIST, HTTP_400_BAD_REQUEST

        user_schema = User.get_schema()
        try:
            user = User(**user_schema.load(request_data))
        except ValidationError as err:
            return err.messages, HTTP_400_BAD_REQUEST

        user.create()

        return user_schema.dump(user), HTTP_201_CREATED

    def put(self, user_id):
        """ Update a user by id """
        request_data = request.get_json()
        user_schema = User.get_schema()
        user = User.query.filter_by(_id=user_id).first_or_404(
            description=USER_NOT_FOUND
        )
        try:
            user.update(user_schema.load(
                request_data, instance=user, partial=True)
            )
        except ValidationError as err:
            return err.messages, HTTP_400_BAD_REQUEST

        return user_schema.dump(user), HTTP_200_OK

    def delete(self, user_id):
        """ Delete a user by id """
        user = User.query.filter_by(_id=user_id).first_or_404(
            description=USER_NOT_FOUND
        )
        user.delete()
        return USER_DELETED_SUCCESS, HTTP_204_NO_CONTENT

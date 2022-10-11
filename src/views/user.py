from pprint import pprint
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src.models.user import User
from src.schema.user import UserSchema
from src.utils.response import SendResponse
from src.utils.user import change_active_status
from src.constants import http_status_codes
from src.constants import user_messages


class UserViews(Resource):
    """User Views for user crud operations"""

    def get(self, user_id: int):
        """ Get a user by id """
        user = User.query.filter_by(
            _id=user_id, active=True
        ).first_or_404(description=user_messages.USER_NOT_FOUND)
        user_schema = UserSchema(only=user_messages.USER_DETAILS)
        serialized_user = user_schema.dump(user)
        return SendResponse(serialized_user), http_status_codes.HTTP_200_OK

    def post(self):
        """ Create a new user """
        user_schema = UserSchema()
        request_data = request.get_json()
        try:
            serialized_user = user_schema.load(request_data)
        except ValidationError as err:
            return SendResponse(err.messages, True), http_status_codes.HTTP_400_BAD_REQUEST

        searched_user = User.query.filter_by(
            email=serialized_user['email']).first()

        if searched_user is not None:
            if searched_user.active:
                return SendResponse(user_messages.USER_ALREADY_EXIST, True), http_status_codes.HTTP_400_BAD_REQUEST
            else:
                return SendResponse(change_active_status(searched_user, serialized_user.get('password'))), http_status_codes.HTTP_200_OK

        user = User(**serialized_user)
        user.create()
        deserialize_user = user_schema.dump(user)
        return SendResponse(deserialize_user), http_status_codes.HTTP_201_CREATED

    def put(self, user_id: int):
        """ Update a user by id """
        request_data = request.get_json()
        user_schema = UserSchema(
            only={'password', 'city', 'state', 'zipcode'}, partial=True)
        pprint(user_schema)
        try:
            serialized_user = user_schema.load(request_data)
        except ValidationError as err:
            return SendResponse(err.messages, True), http_status_codes.HTTP_400_BAD_REQUEST

        user = User.query.filter_by(_id=user_id, active=True).first_or_404(
            description=user_messages.USER_NOT_FOUND
        )
        user.update_data(serialized_user)
        return SendResponse(user_schema.dump(user)), http_status_codes.HTTP_200_OK

    def delete(self, user_id: int):
        """ Delete a user by id """
        user = User.query.filter_by(_id=user_id).first_or_404(
            description=user_messages.USER_NOT_FOUND
        )
        change_active_status(user)
        return SendResponse(""), http_status_codes.HTTP_204_NO_CONTENT

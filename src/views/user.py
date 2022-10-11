from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src.models.user import User
from src.schema.user import UserSchema
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

        return UserSchema(user_messages.USER_DETAILS).dump(user), http_status_codes.HTTP_200_OK

    def post(self):
        """ Create a new user """
        request_data = request.get_json()
        searched_user = User.query.filter_by(
            email=request_data['email']).first()
        if searched_user is not None:
            if searched_user.active:
                return user_messages.USER_ALREADY_EXIST, http_status_codes.HTTP_400_BAD_REQUEST
            else:
                return change_active_status(searched_user, request_data.get('password')), http_status_codes.HTTP_200_OK

        user_schema = UserSchema()

        try:
            user = User(**user_schema.load(request_data))
        except ValidationError as err:
            return err.messages, http_status_codes.HTTP_400_BAD_REQUEST

        user.create()

        return user_schema.dump(user), http_status_codes.HTTP_201_CREATED

    def put(self, user_id: int):
        """ Update a user by id """
        request_data = request.get_json()
        user_schema = UserSchema()
        user = User.query.filter_by(_id=user_id, active=True).first_or_404(
            description=user_messages.USER_NOT_FOUND
        )
        if (request_data.get('email') != user.email):
            return user_messages.USER_MAIL_CHANGE_NOT_ALLOWED, http_status_codes.HTTP_400_BAD_REQUEST
        try:
            user.update(user_schema.load(
                request_data, instance=user, partial=True)
            )
        except ValidationError as err:
            return err.messages, http_status_codes.HTTP_400_BAD_REQUEST

        return user_schema.dump(user), http_status_codes.HTTP_200_OK

    def delete(self, user_id: int):
        """ Delete a user by id """
        user = User.query.filter_by(_id=user_id).first_or_404(
            description=user_messages.USER_NOT_FOUND
        )
        change_active_status(user)
        return "", http_status_codes.HTTP_204_NO_CONTENT

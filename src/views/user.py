from email import message
from pprint import pprint
from flask import request, jsonify

from flask_restful import Resource

from src.constants import http_status_codes
from src.constants import user_messages
from src.models.user import User
from marshmallow import ValidationError
from src.schema import restaurant

from src.schema.restaurant import RestaurantSchema
from src.schema.user import UserSchema
from src.utils.user import change_active_status


class UserViews(Resource):

    def get(self, user_id):
        """ Get a user by id """
        user = User.query.filter_by(
            _id=user_id, active=True
        ).first_or_404(description=user_messages.USER_NOT_FOUND)

        return User.get_schema(user_messages.USER_DETAILS).dump(user), http_status_codes.HTTP_200_OK

    def post(self):
        """ Create a new user """
        request_data = request.get_json()
        searched_user = User.query.filter_by(
            email=request_data['email']).first()
        if searched_user is not None:
            if searched_user.active:
                return user_messages.USER_ALREADY_EXIST, http_status_codes.HTTP_400_BAD_REQUEST
            else:
                return change_active_status(searched_user._id), http_status_codes.HTTP_200_OK

        user_schema = User.get_schema()
        try:
            user = User(**user_schema.load(request_data))
        except ValidationError as err:
            return err.messages, http_status_codes.HTTP_400_BAD_REQUEST

        user.create()

        return user_schema.dump(user), http_status_codes.HTTP_201_CREATED

    def put(self, user_id):
        """ Update a user by id """
        request_data = request.get_json()
        user_schema = User.get_schema()
        user = User.query.filter_by(_id=user_id, active=True).first_or_404(
            description=user_messages.USER_NOT_FOUND
        )
        try:
            user.update(user_schema.load(
                request_data, instance=user, partial=True)
            )
        except ValidationError as err:
            return err.messages, http_status_codes.HTTP_400_BAD_REQUEST

        return user_schema.dump(user), http_status_codes.HTTP_200_OK

    def delete(self, user_id):
        """ Delete a user by id """
        change_active_status(user_id)
        return "", http_status_codes.HTTP_204_NO_CONTENT


class UserRestaurantListViews(Resource):

    def get(self, user_id):
        """ Get a list of restaurants for a user """
        user = UserSchema().dump(User.query.filter_by(_id=user_id, active=True).first_or_404(
            description=user_messages.USER_NOT_FOUND)
        )
        return {"restaurants": user.get('restaurants')}, http_status_codes.HTTP_200_OK

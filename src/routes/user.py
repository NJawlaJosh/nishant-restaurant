from pprint import pprint
from flask import request
from flask_restful import Resource

from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from src.models.address import Address
from src.models.user import User
from marshmallow import ValidationError


class UserRoutes(Resource):

    def get(self, user_id):
        user_schema = User.get_schema(
            {'name', 'email', 'city', 'state', 'zipcode', 'balance'})
        user = User.query.filter_by(_id=user_id).first()
        if user is None:
            return {'message': 'User not found'}, HTTP_404_NOT_FOUND
        return user_schema.dump(user), HTTP_200_OK

    def post(self):
        request_data = request.get_json()

        if User.query.filter_by(email=request_data['email']).first() is not None:
            return {'message': 'User already exists'}, HTTP_400_BAD_REQUEST

        user_schema = User.get_schema()
        address_schema = Address.get_schema()
        try:
            # user schema returns a dictionary object
            user = User(**user_schema.load(request_data))

            # ** is used to unpack the dictionary object
        except ValidationError as err:
            return err.messages, HTTP_400_BAD_REQUEST

        user.create()

        return user_schema.dump(user), HTTP_201_CREATED

    def put(self, user_id):
        request_data = request.get_json()
        user_schema = User.get_schema()
        user = User.query.filter_by(_id=user_id).first()
        if user is None:
            return {'message': 'User not found'}, HTTP_404_NOT_FOUND
        try:
            user.update(user_schema.load(
                request_data, instance=user, partial=True))
        except ValidationError as err:
            return err.messages, HTTP_400_BAD_REQUEST

        return user_schema.dump(user), HTTP_200_OK

    def delete(self, user_id):
        user = User.query.filter_by(_id=user_id).first()
        if user is None:
            return {'message': 'User not found'}, HTTP_404_NOT_FOUND
        user.delete()
        return {'message': 'User deleted successfully'}, HTTP_204_NO_CONTENT


# class UserUpdateRoutes(Resource):
#     def put(self, user_id):
#         request_data = request.get_json()
#         user_schema = User.get_schema()
#         user = User.query.filter_by(_id=user_id).first()
#         if user is None:
#             return {'message': 'User not found'}, HTTP_404_NOT_FOUND
#         try:
#             user.update(user_schema.load(
#                 request_data, instance=user, partial=True))
#         except ValidationError as err:
#             return err.messages, HTTP_400_BAD_REQUEST

#         return user_schema.dump(user), HTTP_200_OK


# class GetUserRoutes(Resource):
#     def get(self, user_id):
#         user_schema = User.get_schema(
#             {'name', 'email', 'city', 'state', 'zipcode', 'balance'})
#         user = User.query.filter_by(_id=user_id).first()
#         if user is None:
#             return {'message': 'User not found'}, HTTP_404_NOT_FOUND
#         return user_schema.dump(user), HTTP_200_OK


# class DeleteUserRoutes(Resource):
#     def delete(self, user_id):
#         user = User.query.filter_by(_id=user_id).first()
#         if user is None:
#             return {'message': 'User not found'}, HTTP_404_NOT_FOUND
#         user.delete()
#         return {'message': 'User deleted successfully'}, HTTP_204_NO_CONTENT


# class UserList(Resource):
#     def get(self):
#         return {'message': 'List of users'}, HTTP_200_OK

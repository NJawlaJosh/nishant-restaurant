from flask import request
from flask_restful import Resource

from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from src.models.user import User
from marshmallow import ValidationError


class UserRoutes(Resource):
    def post(self):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        balance = request.form['balance']

        if User.query.filter_by(email=email).first() is not None:
            return {'message': 'User already exists'}, HTTP_400_BAD_REQUEST

        user_schema = User.get_schema()
        try:
            user_schema.load({
                "name": name,
                "email": email,
                "password": password,
                "city": city,
                "state": state,
                "zipcode": zipcode,
                "balance": balance
            })
        except ValidationError as err:
            return err.messages, HTTP_400_BAD_REQUEST

        user = User(name, email, password, city, state, zipcode, balance)
        user.create()

        return user_schema.dump(user), HTTP_201_CREATED


class UserList(Resource):
    def get(self):
        return {'message': 'List of users'}, HTTP_200_OK

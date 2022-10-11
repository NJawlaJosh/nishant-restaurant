from wsgiref import validate
from marshmallow import Schema, fields

from src.constants.restaurant_constants import RESTAURANT_NAME_LENGTH_MAX, RESTAURANT_NAME_LENGTH_MIN


class RestaurantSchema(Schema):
    """Restaurant Schema for restaurant table"""
    class Meta:
        fields = ('_id', 'name', 'owner')

    _id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(
        min=RESTAURANT_NAME_LENGTH_MIN, max=RESTAURANT_NAME_LENGTH_MAX))
    owner = fields.Nested('UserSchema', only=['_id', 'username'])

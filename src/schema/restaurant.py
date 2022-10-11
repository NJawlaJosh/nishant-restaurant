from marshmallow import fields, validate

from src.constants.restaurant_constants import RESTAURANT_NAME_LENGTH_MAX, RESTAURANT_NAME_LENGTH_MIN
from src.schema import BaseSchema


class RestaurantSchema(BaseSchema):
    """Restaurant Schema for restaurant table"""
    class Meta:
        fields = ('_id', 'name', 'owner')

    name = fields.String(required=True, validate=validate.Length(
        min=RESTAURANT_NAME_LENGTH_MIN, max=RESTAURANT_NAME_LENGTH_MAX)
    )
    owner = fields.Nested('UserSchema', only=['_id', 'username'])

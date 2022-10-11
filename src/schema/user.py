from marshmallow import fields, validate, pre_load, EXCLUDE
from werkzeug.security import generate_password_hash


from src.constants.india_states import indian_states
from src.schema import BaseSchema
from src.schema.restaurant import RestaurantSchema
from src.constants.user_constants import NAME_LENGTH_MIN,  NAME_LENGTH_MAX, PASSWORD_LENGTH_MIN,  PASSWORD_LENGTH_MAX,  CITY_LENGTH_MIN,  CITY_LENGTH_MAX, RESTAURANT_FIELDS,  STATE_LENGTH_MIN,  STATE_LENGTH_MAX, ZIPCODE_LENGTH,  BALANCE_MIN,  CITY_REGEX,  NAME_LENGTH_ERROR,  PASSWORD_LENGTH_ERROR,  CITY_LENGTH_ERROR,  CITY_REGEX_ERROR,  STATE_LENGTH_ERROR,  STATE_ONEOF_ERROR,  ZIPCODE_LENGTH_ERROR,  BALANCE_MIN_ERROR


class UserSchema(BaseSchema):
    """User Schema for user table"""
    class Meta:
        model = 'User'
        primary_key = '_id'
        unknown = EXCLUDE

    @pre_load
    def hash_password(self, data, **kwargs):
        if 'password' in data:
            data['password'] = generate_password_hash(data['password'])
        return data

    name = fields.String(
        required=True, validate=validate.Length(min=NAME_LENGTH_MIN, max=NAME_LENGTH_MAX, error=NAME_LENGTH_ERROR)
    )
    email = fields.Email(required=True)
    password = fields.String(
        required=True, validate=validate.Length(min=PASSWORD_LENGTH_MIN, max=PASSWORD_LENGTH_MAX, error=PASSWORD_LENGTH_ERROR)
    )
    city = fields.String(
        required=True, validate=validate.And(validate.Length(min=CITY_LENGTH_MIN, max=CITY_LENGTH_MAX, error=CITY_LENGTH_ERROR), validate.Regexp(CITY_REGEX, error=CITY_REGEX_ERROR))
    )
    state = fields.String(
        required=True, validate=validate.And(validate.Length(min=STATE_LENGTH_MIN, max=STATE_LENGTH_MAX, error=STATE_LENGTH_ERROR), validate.OneOf(indian_states, error=STATE_ONEOF_ERROR))
    )
    zipcode = fields.String(validate=validate.And(validate.Length(
        equal=ZIPCODE_LENGTH, error=ZIPCODE_LENGTH_ERROR), validate.Regexp(r'^\d+$')))
    balance = fields.Float(required=True, validate=validate.Range(
        min=BALANCE_MIN, error=BALANCE_MIN_ERROR)
    )
    restaurants = fields.Nested(
        'RestaurantSchema', many=True, only=RESTAURANT_FIELDS, dump_only=True
    )
    active = fields.Boolean()

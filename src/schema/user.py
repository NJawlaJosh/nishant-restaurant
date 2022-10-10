from marshmallow import fields, validate

from src.schema import ma
from src.constants.india_states import indian_states


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = 'User'
        primary_key = '_id'
    _id = fields.Integer(dump_only=True)
    name = fields.String(
        required=True, validate=validate.And(validate.Length(min=1, max=100, error="Name must be between 1 and 100 characters long"), validate.Regexp(r'^([a-zA-Z]+\s)*[a-zA-Z]+$', error="Name must contain only letters and spaces"))
    )
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.String(
        required=True, validate=validate.Length(min=5, max=300, error="Password must be between 5 and 300 characters long")
    )
    city = fields.String(
        required=True, validate=validate.And(validate.Length(min=2, max=100, error="City must be between 2 and 100 characters long"), validate.Regexp(r'^([a-zA-Z]+\s)*[a-zA-Z]+$', error="City must contain only letters and spaces"))
    )
    state = fields.String(
        required=True, validate=validate.And(validate.Length(min=2, max=100, error="State must be between 2 and 100 characters long"), validate.OneOf(indian_states, error="State must be a valid Indian state"))
    )
    zipcode = fields.Integer(required=True, validate=validate.Range(
        min=10000, max=99999, error="Zipcode must be 5 digits long")
    )
    balance = fields.Float(required=True, validate=validate.Range(
        min=0, error="Balance must be greater than or equal to 0")
    )
    restaurants = fields.Nested('RestaurantSchema', many=True, only=[
                                '_id', 'name'], dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    active = fields.Boolean()

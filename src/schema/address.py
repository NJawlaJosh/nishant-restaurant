from marshmallow import Schema, fields, validate
from src.constants.india_states import indian_states


class AddressSchema(Schema):
    class Meta:
        table = 'addresses'
        fields = ('id', 'user_id', 'address', 'city', 'state',
                  'zipcode', 'created_at', 'updated_at')
        model = 'Address'

    _id = fields.Integer(dump_only=True)
    city = fields.String(
        required=True, validate=validate.And(validate.Length(min=2, max=100, error="City must be between 2 and 100 characters long"), validate.Regexp(r'^([a-zA-Z]+\s)*[a-zA-Z]+$', error="City must contain only letters and spaces")))
    state = fields.String(
        required=True, validate=validate.And(validate.Length(min=2, max=100, error="State must be between 2 and 100 characters long"), validate.OneOf(indian_states, error="State must be a valid Indian state")))
    zipcode = fields.Integer(required=True, validate=validate.Range(
        min=10000, max=99999, error="Zipcode must be 5 digits long"))
    user_id = fields.Integer(required=True)

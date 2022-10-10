from marshmallow import Schema, fields


class RestaurantSchema(Schema):
    class Meta:
        fields = ('_id', 'name', 'owner')

    _id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    owner = fields.Nested('UserSchema', only=['_id', 'username'])

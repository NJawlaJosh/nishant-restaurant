from flask_marshmallow import Marshmallow
from marshmallow import fields
ma = Marshmallow()


class BaseSchema(ma.SQLAlchemySchema):
    """Base Schema for all schemas"""

    _id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

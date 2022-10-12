from flask_marshmallow import Marshmallow
from marshmallow import fields, pre_load
ma = Marshmallow()


class BaseSchema(ma.SQLAlchemySchema):
    """Base Schema for all schemas"""

    _id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @pre_load
    def remove_whitespace(self, data, **kwargs):
        """Remove whitespace from all fields"""
        for key in data:
            if isinstance(data[key], str):
                data[key] = ' '.join(data[key].split())
        return data

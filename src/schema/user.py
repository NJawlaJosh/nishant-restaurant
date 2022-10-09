from functools import partial
from marshmallow import fields, validate, INCLUDE
# here we have created a Marshmallow object named ma which is used to serialize and deserialize the data from the database to the json format and vice versa and to validate the data before it is inserted into the database and to validate the data before it is updated in the database and to validate the data before it is deleted from the database and to validate the data before it is retrieved from the database and to validate the data before it is displayed on the web page and to validate the data before it is sent to the client side
# serialization is the process of converting the data from the database to the json format
# deserialization is the process of converting the data from the json format to the database
# validation is the process of checking whether the data is valid or not

from src.schema import ma


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        # here we have created a Meta class which is used to specify the table name and the primary key of the table
        # here we have specified the table name as User and the primary key as id
        model = 'User'
        # here we have specified the table name as User
        # here we have specified the primary key as id
        primary_key = '_id'
        load_instance = True
        # here we have specified the load_instance as True as we want to load the instance of the model class User into the UserSchema class
        include_fk = True  # include foreign keys in the schema and the foreign keys are the fields which are used to establish the relationship between the tables
        # include relationships in the schema and the relationships are the fields which are used to establish the relationship between the tables
        include_relationships = True
        unknown = INCLUDE
    _id = fields.Integer(dump_only=True)
    name = fields.String(
        required=True, validate=validate.And(validate.Length(min=1, max=100, error="Name must be between 1 and 100 characters long"), validate.Regexp(r'^([a-zA-Z]+\s)*[a-zA-Z]+$', error="Name must contain only letters and spaces")))
    email = fields.Email(
        required=True, validate=validate.Email())
    password = fields.String(
        required=True, validate=validate.Length(min=5, max=300, error="Password must be between 5 and 300 characters long"))
    balance = fields.Float(required=True, partial=True, validate=validate.Range(
        min=0, error="Balance must be greater than or equal to 0"))
    # fields.Nested takes the name of the schema class as the argument and the many argument is used to specify whether the relationship is one to one or one to many or many to many other arguments are dump_only and load_only
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    # dump_only is a special attribute which is used to specify that the column is not to be included in the deserialization process by default it is set to False
    # load_only is a special attribute which is used to specify that the column is not to be included in the serialization process by default it is set to False
    # here we have created a class named UserSchema which is a child class of Schema class which is a child class of the marshmallow.Schema class

from marshmallow import fields, validate
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
    _id = fields.Integer(dump_only=True)
    name = fields.String(
        required=True, validate=validate.Length(min=1, max=100, error="Name must be between 1 and 100 characters long"))
    email = fields.Email(
        required=True, validate=validate.Email())
    password = fields.String(
        required=True, validate=validate.Length(min=5, max=300, error="Password must be between 5 and 300 characters long"))
    city = fields.String(
        required=True, validate=validate.Length(min=2, max=100, error="City must be between 2 and 100 characters long"))
    state = fields.String(
        required=True, validate=validate.Length(min=2, max=100, error="State must be between 2 and 100 characters long"))
    zipcode = fields.Integer(required=True, validate=validate.Range(
        min=10000, max=99999, error="Zipcode must be 5 digits long"))
    balance = fields.Float(required=True, validate=validate.Range(
        min=0, error="Balance must be greater than or equal to 0"))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    # dump_only is a special attribute which is used to specify that the column is not to be included in the deserialization process by default it is set to False
    # load_only is a special attribute which is used to specify that the column is not to be included in the serialization process by default it is set to False
    # here we have created a class named UserSchema which is a child class of Schema class which is a child class of the marshmallow.Schema class

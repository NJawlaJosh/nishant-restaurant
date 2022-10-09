from src.models.address import Address
from . import db

from src.schema.user import UserSchema


# here we have assigned the db object to SQLAlchemy() class which is a class of flask_sqlalchemy module
# it is used to create a database object which is used to create a database
# we could have used any name for the database object but it is a convention to use db as the name of the database object


class User(db.Model):
    __tablename__ = 'users'
    # here we have created a class named User which is a child class of db.Model class
    # we have assigned the __tablename__ attribute to 'users' which is the name of the table in the database
    # __tablename__ is a special attribute which is used to assign the name of the table in the database
    # special attributes are attributes which are used by the python interpreter to perform some special tasks
    _id = db.Column(db.Integer, primary_key=True)
    # here we have created a column named _id which is of type Integer and is the primary key of the table
    # autoincrement is set to True by default
    # other attributes of the Column class are nullable, unique, default, onupdate, server_default, server_onupdate, index, primary_key, info, key, doc
    # server_default and server_onupdate are used to set the default value and the value to be updated on the server side
    # index is used to create an index on the column in the database used to improve the performance of the database
    # how does index work? index is a data structure which is used to store the values of the column in the table in a sorted order so that the values can be searched in O(log n) time instead of O(n) time which is the time taken to search the values in the table in a linear fashion
    # data structure of index is a binary search tree
    name = db.Column(db.String(100), nullable=False)
    # nullable default value is True
    # if nullable is false then the column cannot have a null value, if it has a null value then an error will be raised but if nullable is true then the column can have a null value
    # unique default value is False
    # default default value is None
    # onupdate default value is None
    # info default value is None
    # key default value is None
    # doc default value is None
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    balance = db.Column(db.Float(), default=0, nullable=False)
    address = db.relationship('Address', backref='user', lazy=True)
    # db. relationship takes following arguments as input
    # here we have created a column named state which is of type Enum
    # values_callable is a special attribute which is used to assign the values of the Enum class to the column
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    # here we have created a column named created_at which is of type DateTime and is not nullable and has a default value of the current time
    # db.func.now() is a function which returns the current time in the database server side and not in the client side which is the time when the request is made to the server and not the time when the request is processed by the server and the response is sent to the client side
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=db.func.now(), onupdate=db.func.now())

    def __init__(self, **kwargs) -> None:
        super().__init__()
        # here we have created a constructor for the User class
        # the constructor is used to initialize the attributes of the class when an object of the class is created using the class name and the constructor is called automatically when an object of the class is created
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.balance = kwargs.get('balance')

    def create(self):
        db.session.add(self)
        # session is a temporary staging area where we can store objects before committing them to the database
        # here we have added the object of the User class to the session object of the database object db
        # session  has a method named add which is used to add the object to the session
        # address = Address()
        db.session.commit()
        # here we have committed the changes made to the session object to the database
        return self

    def update(self, updated_data):
        for key, value in updated_data.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def __repr__(self) -> str:
        return super().__repr__()
    # here super().__repr__() is a function which returns the string representation of the object of the class
    # __repr__() is a special function which is used to return the string representation of the object of the class
    # special functions are functions which are used by the python interpreter to perform some special tasks like __init__() is a special function which is used to initialize the attributes of the class when an object of the class is created using the class name and __repr__() is a special function which is used to return the string representation of the object of the class when the print() function is used to print the object of the class or when the str() function is used to convert the object of the class to a string

    def get_schema(params=None):
        if params:
            return UserSchema(only=params)
        return UserSchema()

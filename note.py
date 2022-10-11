# user schema file

# here we have created a Marshmallow object named ma which is used to serialize and deserialize the data from the database to the json format and vice versa and to validate the data before it is inserted into the database and to validate the data before it is updated in the database and to validate the data before it is deleted from the database and to validate the data before it is retrieved from the database and to validate the data before it is displayed on the web page and to validate the data before it is sent to the client side
# serialization is the process of converting the data from the database to the json format
# deserialization is the process of converting the data from the json format to the database
# validation is the process of checking whether the data is valid or not


# here we have created a Meta class which is used to specify the table name and the primary key of the table
# here we have specified the table name as User and the primary key as id

# dump_only is a special attribute which is used to specify that the column is not to be included in the deserialization process by default it is set to False
# load_only is a special attribute which is used to specify that the column is not to be included in the serialization process by default it is set to False
# here we have created a class named UserSchema which is a child class of Schema class which is a child class of the marshmallow.Schema class

# Flask will look for instance folder in the path of the src instance folder
# and will load the config.py file from there
# FLask takes two arguments, the name of the application module or package
# and the second is the path to the instance folder
# The instance folder is located outside the src package and can hold local data
# that shouldn't be committed to version control, such as configuration secrets
# and the database file
# instance_relative_config=True tells the app that config files are relative
# to the instance folder
# test config is used for testing, purposes only

# here we have assigned the app object to the app attribute of the db object
# by doing this we can access the app object from the db object without this we cannot access the app object from the db object
# we need to access the app object from the db object to initialize the database

# here we have initialized the db object with the app object by passing the app object as an argument to the init_app()
# init_app() is a special method which is used to initialize the db object with the app object
# db object is initialized with the app object so that the db object can access the app object
# if init_app() is used without app parameter then the db object will not be initialized with the app object

# here we have initialized the ma object with the app object by passing the app object as an argument to the init_app()

# app_context() is a special method which is used to create a context for the app object and returns the context object which is then used to create the database tables using the create_all() method of the db object
# with statement is used to create a context for the app object

# here we have initialized the api object with the app object by passing the app object as an argument to the init_app()

# here we have created a class named User which is a child class of db.Model class
# we have assigned the __tablename__ attribute to 'users' which is the name of the table in the database
# __tablename__ is a special attribute which is used to assign the name of the table in the database
# special attributes are attributes which are used by the python interpreter to perform some special tasks

# here we have created a column named _id which is of type Integer and is the primary key of the table
# autoincrement is set to True by default
# other attributes of the Column class are nullable, unique, default, onupdate, server_default, server_onupdate, index, primary_key, info, key, doc
# server_default and server_onupdate are used to set the default value and the value to be updated on the server side
# index is used to create an index on the column in the database used to improve the performance of the database
# how does index work? index is a data structure which is used to store the values of the column in the table in a sorted order so that the values can be searched in O(log n) time instead of O(n) time which is the time taken to search the values in the table in a linear fashion
# data structure of index is a binary search tree

# nullable default value is True
# if nullable is false then the column cannot have a null value, if it has a null value then an error will be raised but if nullable is true then the column can have a null value
# unique default value is False
# default default value is None
# onupdate default value is None
# info default value is None
# key default value is None
# doc default value is None

# here we have created a column named state which is of type Enum
# values_callable is a special attribute which is used to assign the values of the Enum class to the column

# here we have created a column named created_at which is of type DateTime and is not nullable and has a default value of the current time
# db.func.now() is a function which returns the current time in the database server side and not in the client side which is the time when the request is made to the server and not the time when the request is processed by the server and the response is sent to the client side

# session is a temporary staging area where we can store objects before committing them to the database
# here we have added the object of the User class to the session object of the database object db
# session  has a method named add which is used to add the object to the session

# here we have committed the changes made to the session object to the database

# here super().__repr__() is a function which returns the string representation of the object of the class
# __repr__() is a special function which is used to return the string representation of the object of the class
# special functions are functions which are used by the python interpreter to perform some special tasks like __init__() is a special function which is used to initialize the attributes of the class when an object of the class is created using the class name and __repr__() is a special function which is used to return the string representation of the object of the class when the print() function is used to print the object of the class or when the str() function is used to convert the object of the class to a string

# here we have assigned the db object to SQLAlchemy() class which is a class of flask_sqlalchemy module
# it is used to create a database object which is used to create a database
# we could have used any name for the database object but it is a convention to use db as the name of the database object

# user schema returns a dictionary object

# ** is used to unpack the dictionary object

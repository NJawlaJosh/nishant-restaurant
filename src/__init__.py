import os
from flask import Flask
from src.models import db
from src.schema import ma
from src.routes import api


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
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
    if test_config is None:
        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DB_URI'),
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    # here we have assigned the app object to the app attribute of the db object
    # by doing this we can access the app object from the db object without this we cannot access the app object from the db object
    # we need to access the app object from the db object to initialize the database
    db.init_app(app)
    # here we have initialized the db object with the app object by passing the app object as an argument to the init_app()
    # init_app() is a special method which is used to initialize the db object with the app object
    # db object is initialized with the app object so that the db object can access the app object
    # if init_app() is used without app parameter then the db object will not be initialized with the app object
    ma.init_app(app)
    # here we have initialized the ma object with the app object by passing the app object as an argument to the init_app()
    api.init_app(app)
    # here we have initialized the api object with the app object by passing the app object as an argument to the init_app()

    with app.app_context():
        db.create_all()
    # app_context() is a special method which is used to create a context for the app object and returns the context object which is then used to create the database tables using the create_all() method of the db object
    # with statement is used to create a context for the app object

    return app

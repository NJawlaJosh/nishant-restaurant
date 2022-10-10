import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from src.models import db
from src.schema import ma
from src.views import api
from src.models.user import User
from src.models.restaurant import Restaurant


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DB_URI'),
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Restaurant, db.session))

    with app.app_context():
        db.create_all()

    return app

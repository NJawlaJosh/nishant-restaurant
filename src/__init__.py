import os

from flask import Flask

from src.models import db
from src.schema import ma
from src.views import api


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DB_URI'),
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    return app

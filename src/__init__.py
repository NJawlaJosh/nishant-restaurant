import os

from flask import Flask

from src.models import db
from src.schema import ma
from src.views import api
from src.admin import create_admin


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DB_URI'),
        )
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    create_admin(app)

    with app.app_context():
        db.create_all()

    return app

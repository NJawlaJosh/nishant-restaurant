from src.constants.restaurant_constants import RESTAURANT_NAME_LENGTH
from src.models import BaseClass, db


class Restaurant(BaseClass):
    """Restaurant Model for restaurants table"""
    __tablename__ = 'restaurants'
    name = db.Column(db.String(RESTAURANT_NAME_LENGTH), index=True)
    owner = db.Column(db.Integer, db.ForeignKey('users._id'), nullable=False)

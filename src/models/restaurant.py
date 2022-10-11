from src.constants.restaurant_constants import RESTAURANT_NAME_LENGTH
from . import db


class Restaurant(db.Model):
    """Restaurant Model for restaurants table"""
    __tablename__ = 'restaurants'
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(RESTAURANT_NAME_LENGTH), index=True)
    owner = db.Column(db.Integer, db.ForeignKey('users._id'), nullable=False)

    def __repr__(self):
        return f"Restaurant('{self.name}')"

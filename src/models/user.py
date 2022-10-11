from src.models import BaseClass, db

from src.schema.user import UserSchema


class User(BaseClass):
    """User Model for users table"""
    class Meta:
        fields = ({'name', 'email', 'password',
                   'balance', 'city', 'state', 'zipcode'}
                  )
    __tablename__ = 'users'
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    balance = db.Column(db.Float(), default=0, nullable=False)
    restaurants = db.relationship('Restaurant', backref='user', lazy=True)
    active = db.Column(db.Boolean(), default=True, nullable=False)

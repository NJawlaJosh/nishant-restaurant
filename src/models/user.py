from dataclasses import fields
from . import db

from src.schema.user import UserSchema


class User(db.Model):
    class Meta:
        fields = ({'name', 'email', 'password',
                   'balance', 'city', 'state', 'zipcode'}
                  )
    __tablename__ = 'users'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer(), nullable=False)
    balance = db.Column(db.Float(), default=0, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=db.func.now(), onupdate=db.func.now()
                           )

    def __init__(self, name, email, password, city, state, zipcode, balance) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.balance = balance

    def create(self):
        db.session.add(self)
        db.session.commit()
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

    def get_schema(params=None):
        if params:
            return UserSchema(only=params)
        return UserSchema()

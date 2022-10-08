from src.schema.address import AddressSchema
from . import db


class Address(db.Model):
    __tablename__ = 'address'
    _id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users._id'), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, address, city, state, zipcode) -> None:
        super().__init__()
        self.user_id = user_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

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

    def get_schema(params=None):
        if params is None:
            return AddressSchema()
        return AddressSchema(params)

    def __repr__(self) -> str:
        return super().__repr__()

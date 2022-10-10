from . import db


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    owner = db.Column(db.Integer, db.ForeignKey('users._id'), nullable=False)

    def __repr__(self):
        return f"Restaurant('{self.name}')"

import abc

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseClass(db.Model):
    __abstract__ = True
    __tablename__ = abc.abstractproperty()
    __metaclass__ = abc.ABCMeta

    _id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=db.func.now(), onupdate=db.func.now()
                           )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update_data(self, updated_data=None):
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

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.admin.models import AdminUserView

from src.models import db
from src.models.user import User
from src.models.restaurant import Restaurant


def create_admin(app):
    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    admin.add_view(AdminUserView(User, db.session))
    admin.add_view(ModelView(Restaurant, db.session))
    return admin

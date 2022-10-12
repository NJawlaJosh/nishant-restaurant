from flask_admin.contrib.sqla import ModelView


class AdminUserView(ModelView):
    column_exclude_list = ['password']

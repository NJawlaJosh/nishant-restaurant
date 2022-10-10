from src.models.user import User
from src.constants import user_messages


def change_active_status(user, password=None):
    """ Change the active status of a user """
    user.active = not user.active
    if password:
        user.password = password
    user.update()
    user_schema = User.get_schema()
    return user_schema.dump(user)

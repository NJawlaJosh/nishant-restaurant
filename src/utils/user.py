from src.models.user import User
from src.constants import user_messages


def change_active_status(user_id):
    """ Change the active status of a user """
    user = User.query.filter_by(_id=user_id).first_or_404(
        description=user_messages.USER_NOT_FOUND
    )
    user.active = not user.active
    user.update()
    user_schema = User.get_schema()
    return user_schema.dump(user)

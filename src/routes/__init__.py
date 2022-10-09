from flask_restful import Api
from .user import UserRoutes
api = Api()

# api.add_resource(GetUserRoutes, '/user/<int:user_id>')
api.add_resource(UserRoutes, '/user', '/users/<int:user_id>',
                 '/user/<int:user_id>')
# api.add_resource(UserUpdateRoutes, '/users/<int:user_id>')
# api.add_resource(DeleteUserRoutes, '/user/<int:user_id>')

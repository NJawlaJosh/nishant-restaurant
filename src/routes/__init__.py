from flask_restful import Api
from .user import UserRoutes, UserList, UserUpdateRoutes, GetUserRoutes
api = Api()

api.add_resource(GetUserRoutes, '/user/<int:user_id>')
api.add_resource(UserRoutes, '/user')
api.add_resource(UserUpdateRoutes, '/users/<int:user_id>')

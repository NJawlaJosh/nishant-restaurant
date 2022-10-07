from flask_restful import Api
from .user import UserRoutes, UserList
api = Api()


api.add_resource(UserRoutes, '/user')
api.add_resource(UserList, '/users')

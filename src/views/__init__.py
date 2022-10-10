from flask_restful import Api

from .user import UserViews


api = Api()
api.add_resource(UserViews, '/user', '/users/<int:user_id>',
                 '/user/<int:user_id>'
                 )

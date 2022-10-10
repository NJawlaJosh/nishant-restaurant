from flask_restful import Api

from .user import UserRestaurantListViews, UserViews


api = Api()
api.add_resource(UserViews, '/user', '/users/<int:user_id>',
                 '/user/<int:user_id>'
                 )
api.add_resource(UserRestaurantListViews, '/user/restaurants/<int:user_id>')

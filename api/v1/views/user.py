from flask import jsonify, abort
from api.v1.views import api_views
from models import storage
from models.user import User

@api_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieve a list of all users"""
    all_users = storage.all(User).values()
    users_list = []
    for user in all_users:
        users_list.append(user.to_dict())
    return jsonify(users_list)

@api_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

from flask import Blueprint

api_views = Blueprint("api_views", __name__, url_prefix="/api/v1")

from api.v1.views import course, user
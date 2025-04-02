from flask import jsonify, abort
from api.v1.views import api_views
from models import storage
from models.course import Course

@api_views.route('/courses', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieve a list of all users"""
    all_courses = storage.all(Course).values()
    course_list = []
    for course in all_courses:
        course_list.append(course.to_dict())
    return jsonify(course_list)

@api_views.route('/courses/<course_id>', methods=['GET'], strict_slashes=False)
def get_user(course_id):
    """Retrieve a course"""
    course = storage.get(Course, course_id)
    if not course:
        abort(404)
    return jsonify(course.to_dict())

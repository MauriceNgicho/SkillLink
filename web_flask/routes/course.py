from flask import Blueprint, render_template
from models import storage
from models.course import Course

course = Blueprint("course", __name__, url_prefix="/course")

@course.route("/courses")
def list_courses():
    courses = storage.session.query(Course).all()
    return render_template("courses.html", courses=courses)

@course.route("/home")
def home():
    courses = storage.session.query(Course).all()
    return render_template("home.html", courses=courses)

@course.route("/<course_id>")
def view_course(course_id):
    course = storage.session.get(Course, course_id)
    if not course:
        return "Course not found", 404
    is_enrolled = False

    return render_template("course_detail.html", course=course, is_enrolled=is_enrolled)

@course.route("/<course_id>/enroll")
def enroll(course_id):
    """Enroll the user in the course."""
    course = storage.session.get(Course, course_id)
    if not course:
        return "Course not found", 404
    return f"You have enrolled in {course.title}!"

from flask import Blueprint, render_template
from models import storage
from models.lesson import Lesson

lesson = Blueprint("lesson", __name__, url_prefix="/lesson")

@lesson.route("/<lesson_id>")
def view_lesson(lesson_id):
    """Display a lesson"""
    lesson = storage.session.get(Lesson, lesson_id)
    if not lesson:
        return "Lesson not found", 404
    return render_template("lesson_detail.html", lesson=lesson)
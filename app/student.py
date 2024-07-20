from flask import Blueprint, url_for, redirect

student_bp = Blueprint('student', __name__, url_prefix='/')
@student_bp.route("/")
def home():
    return redirect(url_for('admin.index'))
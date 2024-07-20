from flask import Blueprint, url_for, redirect

student_bp = Blueprint('admin', __name__, url_prefix='/admin/')
@student_bp.route("/")
def home():
    return redirect(url_for('admin.index'))
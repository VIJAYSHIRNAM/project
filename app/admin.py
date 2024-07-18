from flask import Blueprint, render_template, redirect

admin_bp = Blueprint('admin', __name__, url_prefix='/admin/')


@admin_bp.route("/")
def home():
    return render_template("admin/home.html")


@admin_bp.route("/add_student/")
def add_student():
    return render_template("admin/add_student.html")


@admin_bp.route("/index")
def index():
    return redirect('home')


@admin_bp.route("/attendance/")
def take_attendance():
    return render_template("admin/take_attendance.html")


@admin_bp.route("/about")
def about():
    return redirect('home')

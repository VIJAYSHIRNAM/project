from flask import Blueprint, render_template, redirect, request
import json
from app.utility.image_util import create_image_from_bytes, base64_to_image, show_image
from app.utility.common_util import immutable_to_dict

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


@admin_bp.route("/register_student/", methods=["POST"])
def register_student():
    data = immutable_to_dict(request.form)
    with open("dummy.json", "w") as writer:
        json.dump(data, writer)
    for img in data["images[]"]:
        show_image(create_image_from_bytes(base64_to_image(img)))
    return "The Data Received Successfully !"


@admin_bp.route("/about")
def about():
    return redirect('home')

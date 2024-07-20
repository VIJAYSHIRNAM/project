from flask import Flask

from app.admin import admin_bp
from app.student import student_bp

def create_ams_app():

    app = Flask(__name__)
    app.template_folder = "../templates"
    app.static_folder = "../static"
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)
    return app
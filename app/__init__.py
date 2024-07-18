from flask import Flask

from app.admin import admin_bp

def create_ams_app():

    app = Flask(__name__)
    app.template_folder = "../templates"
    app.static_folder = "../static"
    app.register_blueprint(admin_bp)
    return app
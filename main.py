from flask import Flask, render_template, redirect

ams_app = Flask(__name__)


@ams_app.route("/")
def home():
    return render_template("home.html")

@ams_app.route("/add_student/")
def add_student():
    return render_template("add_student.html")
@ams_app.route("/index")
def index():
    return redirect('home')

@ams_app.route("/attendance/")
def take_attendance():
    return render_template("take_attendance.html")

@ams_app.route("/about")
def about():
    return redirect('home')

if __name__ == "__main__":
    ams_app.run(debug=True)

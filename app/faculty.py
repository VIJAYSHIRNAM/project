from flask import Blueprint, render_template, redirect, Response, current_app

faculty_bp = Blueprint('faculty', __name__, url_prefix='/faculty/')

@faculty_bp.route("/")
def home():
    return render_template("faculty/home.html")

def stop_cam():
    detector = current_app.config['detector']
    if detector.cap and detector.cap.isOpened():
        print("Released !")
        detector.cap.release()

@faculty_bp.route('/stop',methods=['POST'])
def stop():
    detector = current_app.config['detector']
    if detector.cap and detector.cap.isOpened():
        detector.cap.release()
    return "Done !"

@faculty_bp.route('/start',methods=['POST'])
def start():
    stop()
    return render_template('faculty/detector.html')

@faculty_bp.route("/attendance/")
def take_attendance():
    stop()
    return render_template("faculty/take_attendance.html")
@faculty_bp.route('/video_capture')
def video_capture():
    detector = current_app.config['detector']
    return Response(detector.capture_by_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@faculty_bp.route("/profile")
def about():
    return redirect('home')
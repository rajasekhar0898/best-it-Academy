from flask import flash, session, redirect, render_template, Blueprint, current_app,send_from_directory,Response
import os
from flask_wtf.csrf import generate_csrf
from flask_login import login_required,current_user

course_bp = Blueprint("course", __name__)

@course_bp.route("/python_course", methods=["GET", "POST"])
@login_required
def python_course():
    csrf_token = generate_csrf()
    if 'username' not in session:
        flash("Please log in first.")
        return redirect('/student_login')
    
    username = session.get('username')
    course = session.get('course')
    
    # Retrieve upload folder paths from the Flask application configuration
    upload_folders = current_app.config.get('UPLOAD_FOLDERS', {}).get('python', {})
    
    # Ensure that all upload folders exist; if not, create them
    for folder_name, folder_path in upload_folders.items():
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Get the list of files in each upload folder
    file_notes = os.listdir(upload_folders.get('notes', ''))
    file_recordings = os.listdir(upload_folders.get('recordings', ''))
    file_assignments = os.listdir(upload_folders.get('assignments', ''))
    file_assessments = os.listdir(upload_folders.get('assessments', ''))
    
    return render_template("python_course.html", username=username, course=course, 
                           file_notes=file_notes, file_recordings=file_recordings, 
                           file_assignments=file_assignments, file_assessments=file_assessments, csrf_token=csrf_token,currrent_user=current_user)

@course_bp.route("/java_course", methods=["GET", "POST"])
def java_course():
    csrf_token = generate_csrf()
    if 'username' not in session:
        flash("Please log in first.")
        return redirect('/student_login')
    
    username = session.get('username')
    course = session.get('course')
    
    # Retrieve upload folder paths from the Flask application configuration
    upload_folders = current_app.config.get('UPLOAD_FOLDERS', {}).get('java', {})
    
    # Ensure that all upload folders exist; if not, create them
    for folder_name, folder_path in upload_folders.items():
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Get the list of files in each upload folder
    file_notes = os.listdir(upload_folders.get('notes', ''))
    file_recordings = os.listdir(upload_folders.get('recordings', ''))
    file_assignments = os.listdir(upload_folders.get('assignments', ''))
    file_assessments = os.listdir(upload_folders.get('assessments', ''))
    
    return render_template("java_course.html", username=username, course=course, 
                           file_notes=file_notes, file_recordings=file_recordings, 
                           file_assignments=file_assignments, file_assessments=file_assessments, csrf_token=csrf_token)
    
    


@course_bp.route("/digitalmarketing_course", methods=["GET", "POST"])
def DM_course():
    csrf_token = generate_csrf()
    if 'username' not in session:
        flash("Please log in first.")
        return redirect('/student_login')
    
    username = session.get('username')
    course = session.get('course')
    
    # Retrieve upload folder paths from the Flask application configuration
    upload_folders = current_app.config.get('UPLOAD_FOLDERS', {}).get('digitalmarketing', {})
    
    # Ensure that all upload folders exist; if not, create them
    for folder_name, folder_path in upload_folders.items():
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Get the list of files in each upload folder
    file_notes = os.listdir(upload_folders.get('notes', ''))
    file_recordings = os.listdir(upload_folders.get('recordings', ''))
    file_assignments = os.listdir(upload_folders.get('assignments', ''))
    file_assessments = os.listdir(upload_folders.get('assessments', ''))
    
    return render_template("DM_course.html", username=username, course=course, 
                           file_notes=file_notes, file_recordings=file_recordings, 
                           file_assignments=file_assignments, file_assessments=file_assessments, csrf_token=csrf_token)
    
    
    
    
@course_bp.route("/testingtools_course", methods=["GET", "POST"])
def TT_course():
    csrf_token = generate_csrf()
    if 'username' not in session:
        flash("Please log in first.")
        return redirect('/student_login')
    
    username = session.get('username')
    course = session.get('course')
    
    # Retrieve upload folder paths from the Flask application configuration
    upload_folders = current_app.config.get('UPLOAD_FOLDERS', {}).get('testingtools', {})
    
    # Ensure that all upload folders exist; if not, create them
    for folder_name, folder_path in upload_folders.items():
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Get the list of files in each upload folder
    file_notes = os.listdir(upload_folders.get('notes', ''))
    file_recordings = os.listdir(upload_folders.get('recordings', ''))
    file_assignments = os.listdir(upload_folders.get('assignments', ''))
    file_assessments = os.listdir(upload_folders.get('assessments', ''))
    
    return render_template("TT_course.html", username=username, course=course, 
                           file_notes=file_notes, file_recordings=file_recordings, 
                           file_assignments=file_assignments, file_assessments=file_assessments, csrf_token=csrf_token)
    
    
"""
another process to download files from  directory 

@course_bp.route('/<course>/<file_type>/<filename>', methods=["GET", "POST"])
@login_required
def course_file(course, file_type, filename):
    print(f"Course received: {course}")
    print(f"File type received: {file_type}")

    course_folders = current_app.config.get('UPLOAD_FOLDERS', {}).get(course)
    if not course_folders:
        print(f"Course '{course}' is not valid")
        return "Course not found", 404

    upload_folder = course_folders.get(file_type)
    if not upload_folder:
        print(f"File type '{file_type}' is not valid for course '{course}'")
        return "File type not found", 404

    file_path = os.path.join(upload_folder, filename)
    print(f"Upload folder: {upload_folder}")
    print(f"File path: {file_path}")

    if os.path.exists(file_path):
        print(f"File '{filename}' exists at '{file_path}'")
        return "existed"
    else:
        print(f"File '{filename}' not found at '{file_path}'")
        return "File not found", 404
        """

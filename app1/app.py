# app/__init__.py
from flask import Flask
from app1.extensions.db import db
from app1.configure import Config
from app1.extensions.login_manager import login_manager
from app1.routes import main, student, faculty, stu_course, uploads


def load_config(app):
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://avnadmin:AVNS_dro4YtU_Jx8pbFN0OOc@mysql-class-rajasekharvadlamudi57-d7cd.a.aivencloud.com:12873/defaultdb'
    

def create_app():
    server = Flask(__name__)
    load_config(server)
    server.config.from_object(Config)
    login_manager.init_app(server)  # Initialize login manager
    db.init_app(server)
    with server.app_context():
        db.create_all()
    register_blueprints(server)
    return server

def register_blueprints(app):
    app.register_blueprint(main.main_bp)
    app.register_blueprint(student.student_bp)
    app.register_blueprint(faculty.faculty_bp)
    app.register_blueprint(stu_course.course_bp)
    app.register_blueprint(uploads.uploads_bp)
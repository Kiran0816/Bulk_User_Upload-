import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_database(app, db_uri=None):
    if db_uri is None:
        db_uri = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    passwordhash = db.Column(db.String(255))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    roleid = db.Column(db.Integer)
    departmentid = db.Column(db.Integer)
    isactive = db.Column(db.Integer)
    lastlogin = db.Column(db.DateTime)
    createdat = db.Column(db.DateTime)
    updatedat = db.Column(db.DateTime)
    profilepictureurl = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    timezone = db.Column(db.String(50))
    language = db.Column(db.String(50))

def create_tables(db_instance):
    with db_instance.app.app_context():
        db_instance.create_all()


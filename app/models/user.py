# app/models/user.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 对于学生，这是学号
    username = db.Column(db.String(80), unique=True)  # 可以是学号、教师名或TA名
    hashed_password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))

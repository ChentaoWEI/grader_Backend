# app/models/student.py
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 学号
    password = db.Column(db.String(50))


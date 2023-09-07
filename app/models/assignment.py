from app import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    file_path = db.Column(db.String(255))  # 存储作业文件的路径
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'))  # 教师或TA的ID

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'))
    file_path = db.Column(db.String(255))  # 存储学生提交的文件的路径

    
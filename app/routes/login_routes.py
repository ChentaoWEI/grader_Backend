from flask import request, session, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, app
from app.models.user import User
from app.models.role import Role
from flask import render_template

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    plain_password = request.form.get('password')
    role_name = request.form.get('role')  # 这里的role可以是'Student', 'Teacher', 或 'TA'

    role = Role.query.filter_by(name=role_name).first()
    if not role:
        return "Invalid role!", 400

    hashed_password = generate_password_hash(plain_password)
    user = User(username=username, hashed_password=hashed_password, role=role)

    db.session.add(user)
    db.session.commit()

    return f"{role_name} registered!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    provided_password = request.form.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.hashed_password, provided_password):
        session['user_id'] = user.id
        return f"Logged in as {user.role.name}!"
    else:
        return "Invalid username or password!"

@app.route('/login_page')
def login_page():
    return render_template('login.html')


@app.route('/student/dashboard')
def student_dashboard():
    if 'student_id' in session:
        student_id = session['student_id']
        # ... 获取学生相关信息 ...
        return render_template('student_dashboard.html', student_id=student_id)
    else:
        flash('请先登录!', 'warning')
        return redirect(url_for('student_login'))

# @app.route('/student/register', methods=['POST'])
# def register_student():
#     student_id = request.form.get('student_id')
#     plain_password = request.form.get('password')
#     hashed_password = generate_password_hash(plain_password)

#     student_role = Role.query.filter_by(name='Student').first() # 获取学生角色
#     if not student_role:
#         return "Student role not found!", 500

#     student = User(id=student_id, hashed_password=hashed_password, role=student_role)
#     db.session.add(student)
#     db.session.commit()

#     return "Student registered!"

# @app.route('/student/login', methods=['POST'])
# def student_login():
#     student_id = request.form.get('student_id')
#     provided_password = request.form.get('password')
    
#     student = User.query.filter_by(id=student_id).first()
    
#     if student and check_password_hash(student.hashed_password, provided_password):
#         session['student_id'] = student.id
#         return "Logged in successfully!"
#     else:
#         return "Invalid student ID or password!"
# app/routes/student_routes.py
from flask import render_template, request, redirect, url_for, session, flash
from app.models import Student
from app import app

@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        password = request.form.get('password')
        student = Student.query.filter_by(id=student_id).first()
        if student and student.password == password:
            session['student_id'] = student.id
            flash('登录成功!', 'success')
            return redirect(url_for('student_dashboard'))
        else:
            flash('学号或密码错误!', 'danger')
    return render_template('student_login.html')

@app.route('/student/dashboard')
def student_dashboard():
    if 'student_id' in session:
        student_id = session['student_id']
        # ... 获取学生相关信息 ...
        return render_template('student_dashboard.html', student_id=student_id)
    else:
        flash('请先登录!', 'warning')
        return redirect(url_for('student_login'))

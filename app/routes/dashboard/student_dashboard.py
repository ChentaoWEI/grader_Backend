from flask import render_template, request, session, redirect, url_for, flash
from app import app, db
from app.models.assignment import Assignment, Submission

@app.route('/student/dashboard')
def student_dashboard():
    if 'user_id' not in session or session.get('role_name') != 'Student':
        flash('请先登录!', 'warning')
        return redirect(url_for('login_page'))  # 修改为你的登录页面路由

    student_id = session['user_id']
    
    # 获取所有作业和学生的提交状态
    assignments = Assignment.query.all()
    submissions = {sub.assignment_id: sub for sub in Submission.query.filter_by(student_id=student_id)}

    return render_template('student_dashboard.html', student_id=student_id, assignments=assignments, submissions=submissions)

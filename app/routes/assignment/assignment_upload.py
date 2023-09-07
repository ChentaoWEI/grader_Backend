from flask import request, redirect, url_for, flash
import os
from app import app, db
from app.models.assignment import Assignment
from flask import render_template, session
from config import UPLOAD_FOLDER

@app.route('/assignment/upload', methods=['POST'])
def upload_assignment():
    if 'user_id' not in session or session.get('role_name') not in ['Teacher', 'TA']:
        flash('Unauthorized!', 'danger')
        return redirect(url_for('login_page'))

    file = request.files['file']
    title = request.form.get('title')
    description = request.form.get('description')

    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)

        assignment = Assignment(title=title, description=description, file_path=filename, posted_by=session['user_id'])
        db.session.add(assignment)
        db.session.commit()

        flash('Assignment uploaded successfully!', 'success')
    else:
        flash('File upload failed!', 'danger')

    return redirect(url_for('teacher_dashboard'))  # 假设你有一个教师的仪表板路由

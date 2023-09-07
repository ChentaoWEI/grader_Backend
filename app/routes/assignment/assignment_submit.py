from flask import flash, redirect, url_for, request, session
from app import app, db
from app.models.assignment import Assignment, Submission
import os
from config import SUBMISSION_FOLDER

@app.route('/assignment/submit/<int:assignment_id>', methods=['POST'])
def submit_assignment(assignment_id):
    if 'user_id' not in session or session.get('role_name') != 'Student':
        flash('Unauthorized!', 'danger')
        return redirect(url_for('login_page'))

    assignment = Assignment.query.get(assignment_id)
    if not assignment:
        flash('Assignment not found!', 'danger')
        return redirect(url_for('student_dashboard'))  # 假设你有一个学生仪表板路由

    file = request.files['file']

    if file:
        filename = os.path.join(SUBMISSION_FOLDER, file.filename)
        file.save(filename)

        submission = Submission(student_id=session['user_id'], assignment_id=assignment_id, file_path=filename)
        db.session.add(submission)
        db.session.commit()

        flash('Assignment submitted successfully!', 'success')
    else:
        flash('File upload failed!', 'danger')

    return redirect(url_for('student_dashboard'))  # 重定向到学生仪表板

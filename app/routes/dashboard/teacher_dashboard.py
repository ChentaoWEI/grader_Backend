from app.models.assignment import Assignment
from flask import render_template, session, redirect, url_for, flash
from app import app

@app.route('/teacher/dashboard')
def teacher_dashboard():
    if 'user_id' not in session or session.get('role_name') not in ['Teacher', 'TA']:
        flash('Unauthorized!', 'danger')
        return redirect(url_for('login_page'))

    user_id = session['user_id']
    assignments = Assignment.query.filter_by(posted_by=user_id).all()

    return render_template('teacher_dashboard.html', assignments=assignments)



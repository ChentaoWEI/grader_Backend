# run.py
from app import app, db
import sys
from app.models.role import Role

def init_db():
    """Initialize the database with tables and seed data."""
    db.create_all()

    # Check if roles already exist
    if not Role.query.filter_by(name='Student').first():
        student_role = Role(name='Student')
        db.session.add(student_role)

    if not Role.query.filter_by(name='Teacher').first():
        teacher_role = Role(name='Teacher')
        db.session.add(teacher_role)

    if not Role.query.filter_by(name='TA').first():
        ta_role = Role(name='TA')
        db.session.add(ta_role)

    db.session.commit()

    print('Initialized the database.')


# Run a development server using python run.py, initialize the database using python run.py --init-db.
if __name__ == '__main__':
    if '--init-db' in sys.argv:
        init_db()
    else:
        app.run(debug=True)


# run.py
from app import app, db

if __name__ == '__main__':
    db.create_all()  # 创建数据库表
    app.run(debug=True)

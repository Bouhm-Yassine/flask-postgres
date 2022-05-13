from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/test_db"
# SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


@app.route('/save', methods=['POST'])
def save_student():
    post_data = request.json
    student = Student(post_data['fname'], post_data['lname'])
    db.session.add(student)
    db.session.commit()
    return None


@app.route('/get', methods=['GET'])
def get_students():
    students = db.session.query(Student).filter(Student.id == 1)
    for s in students:
        print(s)
    return None


if __name__ == '__main__':
    app.run(debug=True)


# ===> TO CREATE DATABASE
# Go to terminal and enter:
# python
# from application import db
# db.create_all()

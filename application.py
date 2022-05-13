from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/test_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class Menage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menage = db.Column(JSON)


db.create_all()


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     content = db.Column(db.Text)
#     comments = db.relationship('Comment', backref='post')
#
#     def __repr__(self):
#         return f'<Post "{self.title}">'
#
#
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     note = db.Column(db.Integer)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#
#     def __repr__(self):
#         return f'<Comment "{self.content[:20]}...">'


# One Student To Many Notes
# class Student(db.Model):
#     __tablename__ = 'students'
#     id = db.Column(db.Integer, primary_key=True)
#     fname = db.Column(db.String(40))
#     lname = db.Column(db.String(40))
#
#     # notes = relationship("Note")
#     notes = db.relationship('Notes', backref='list', lazy=True)
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#
# class Note(db.Model):
#     __tablename__ = 'notes'
#     id = db.Column(db.Integer, primary_key=True)
#     note = db.Column(db.Integer)
#
#     student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
#
#     # student = relationship("Student", back_populates="notes")
#     def __init__(self, note, student_id):
#         self.note = note
#         self.student_id = student_id


@app.route('/save', methods=['POST'])
def save_student():
    post_data = request.json
    # student = Student(post_data['fname'], post_data['lname'])

    # post1 = Post(title='Post The Third', content='Content for the third post')
    # comment1 = Comment(note=33, post=post1)
    #
    # db.session.add_all([post1])
    # db.session.add_all([comment1])

    menage1 = Menage(menage={"name": "yassine", "age": 23})
    menage2 = Menage(menage={"name": "bouhm", "age": 55, "adresse": {"city": "agadir", "rue": "YAYA HHH"}})
    db.session.add_all([menage1, menage2])
    db.session.commit()
    return None


@app.route('/save', methods=['GET'])
def get_students():
    # menage = Menage.query.first()
    # menages = Menage.query.first()
    # menages = Menage.query.filter(Menage.id == 1).first()
    menages = Menage.query.filter()
    for menage in menages:
        print(menage)
        print(menage.menage)
        print(type(menage.menage['age']))
        print(type(menage.menage))
        print('----------------')
    return None


if __name__ == '__main__':
    app.run(debug=True)

# ===> TO CREATE DATABASE
# Go to terminal and enter:
# python
# from application import db
# db.create_all()

from .db import db
from .student import Student


circle_joins = db.Table(
  'circle_joins',
  db.Model.metadata,
  db.Column('circle_id', db.Integer, db.ForeignKey('circles.id'), primary_key=True),
  db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True)
)


class Circle(db.Model):
  __tablename__ = 'circles'

  id = db.Column(db.Integer, primary_key=True)
  leader_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))

  students = db.relationship(
    'Student',
    secondary=circle_joins,
    backref='circle')

  def to_dict(self):
    return {
      "id": self.id,
      "leader_id": self.leader_id
    }
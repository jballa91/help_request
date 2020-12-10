from .db import db


class Help_Request(db.Model):
  __tablename__ = 'help_requests'

  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text, nullable=False)
  methods_tried = db.Column(db.Text, nullable=False)
  type_id = db.Column(db.Integer, db.ForeignKey('issue_types.id'))
  student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
  circle_id = db.Column(db.Integer, db.ForeignKey('circles.id'))


  def to_dict(self):
    return {
      'id': self.id,
      'description': self.description,
      'methods_tried': self.methods_tried,
      'type_id': self.type_id,
      'student_id': self.student_id,
      'circle_id': self.circle_id
    }
from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Student(db.Model, UserMixin):
  __tablename__ = 'students'

  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  first_name = db.Column(db.String(255), nullable=False)
  last_name = db.Column(db.String(255), nullable=False)
  hashword = db.Column(db.String(255), nullable = False)
  cohort_id = db.Column(db.Integer, db.ForeignKey('cohorts.id'))
  circle_id = db.Column(db.Integer, db.ForeignKey('circles.id'))
  type = db.Column(db.String(255))


  @property
  def password(self):
    return self.hashword


  @password.setter
  def password(self, password):
    self.hashword = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)


  def to_dict(self):
    return {
      "id": self.id,
      "email": self.email
    }

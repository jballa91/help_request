from .db import db


class Issue_Type(db.Model):
  __tablename__ = 'issue_types'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(500))

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name
    }
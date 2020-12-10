from .db import db


class Cohort(db.Model):
  __tablename__ = "cohorts"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  ptm_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'ptm_id': self.ptm_id
    }
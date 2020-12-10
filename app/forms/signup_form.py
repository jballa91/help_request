from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Student


def user_exists(form, field):
    print("Checking if user exits", field.data)
    email = field.data
    user = Student.query.filter(Student.email == email).first()
    if user:
        raise ValidationError("Student is already registered.")


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired()])

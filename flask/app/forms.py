import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append('..')
from wtforms.validators import  ValidationError, Email, EqualTo
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message='please enter your username')])
    password = PasswordField('password', validators=[DataRequired(message='please enter you pwd')])
    remember_me = BooleanField('remember me')
    submit = SubmitField('login')


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('registration')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('duplicated! please re-enter the registration.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('duplicated! re-enter your email')

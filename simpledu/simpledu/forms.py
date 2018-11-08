from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required
from simpledu.models import db, User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators = [Required(), Length(3, 24)])
    email = StringField('Email', validators = [Required(), Email()])
    password = PasswordField('Password', validators = [Required(), Length(6, 512)])
    repeat_password = PasswordField('Password again', validators = [Required(), EqualTo('password')])
    submit = SubmitField('Submit')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Email()])
    password = PasswordField('Password', validators = [Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField, BooleanField, ValidationError, SubmitField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import User, db

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Email()])
#username = StringField('Username', validators = [Required(), Length(3, 24)])
    password = PasswordField('Password', validators = [Required(), Length(6,24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationErron('Username Not Exist or Password Error')
        if field.data and not User.query.filter_by(username = field.data).first():
            raise ValidationError("Username Not Exist")

    def validate_password(self, field):
        user = User.query.filter_by(username = self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password Error')

class RegisterForm(FlaskForm):
	name = StringField('Name', validators = [Required(), Length(3,24)])
	email = StringField('Email', validators = [Required(), Email()])
	password = PasswordField('Password', validators = [Required(), Length(6,24)])
	repeat_password = PasswordField('RepeatPassword', validators = [Required(), EqualTo('password')])
	submit = SubmitField('Submit')

	def validate_username(self, field):
            if User.query.filter_by(name = field.data).first():
                    raise ValidationError('name exist')

	def validate_email(self, field):
            if User.query.filter_by(email = field.data).first():
                    raise ValidationError('email have exist')
	
	def create_user(self):
            user = User(username = self.name.data,
                        email = self.email.data,
                        password = self.password.data)
            db.session.add(user)
            db.session.cimmit()
            return user



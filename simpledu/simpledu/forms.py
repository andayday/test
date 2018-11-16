from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange
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

    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationError('username format error')
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('username already exist')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already exist')



class LoginForm(FlaskForm):
    #email = StringField('Email', validators = [Required(), Email()])
    username = StringField('Username', validators = [Required(), Length(3, 24)])
    password = PasswordField('Password', validators = [Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email = field.data).first():
            raise ValidationError("Email not register")

    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationError('Username Not Exist or Password Error')
        if field.data and not User.query.filter_by(username = field.data).first():
            raise ValidationError("Username Not Exist")
    
    def validate_password(self, field):
        user = User.query.filter_by(username = self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password Error')

class CourseForm(FlaskForm):
    name = StringField('coursename', validators = [Required(), Length(5, 32)])
    description = TextAreaField('coursedescription', validators = [Required(), Length(5, 32)])

    image_url = StringField('image_url', validators = [Required(), URL()])
    author_id = IntegerField('author id', validators = [Required(), NumberRange(min, message='valid id')])

    submit = SubmitField('submit')

    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('user is not exist')

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

        




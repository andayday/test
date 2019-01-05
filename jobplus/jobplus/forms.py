from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField, BooleanField, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [Required(), Length(3, 24)])
    password = PasswordField('Password', validators = [Rquired(), Length(6,24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationErron('Username Not Exist or Password Error')
        if field.data and not User.query.filter_by(username = field.data).first():
            raise ValidationError("Username Not Exist")

    def validate_password(self, field):
        user = User.query.filter_by(username = self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password Error')



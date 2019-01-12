from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField, BooleanField, ValidationError, SubmitField, IntegerField, TextAreaField
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
            db.session.commit()
            return user

class CompanyProfileForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators = [Required(), Email()])
    password = PasswordField('密码（不填写保持不变）')
    slug = StringField('Slug', validators = [Required(), Length(3,24)])
    location = StringField('地址', validators = [Length(0, 64)])
    site = StringField('公司网站', validators = [Length(0, 64)])
    logo = StringField('Logo')
    description = StringField('一句话描述', validators = [Length(0, 100)])
    about = TextAreaField('公司详情', validators = [Length(0, 1024)])
    submit = SubmitField('提交')

    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13', '15', '18') and len(phone) != 11:
            raise ValidationError('请输入有效的手机号')
    def updated_profile(self, user):
        user.username = self.name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data

        if user.company_detail:
            company_detail = user.company_detail
        else:
            company_detail = CompanyDetail()
            company_detail.user_id = user.id

        self.populate_obj(company_detail)
        db.session.add(user)
        db.session.add(company_detail)
        db.session.commit()


class UserProfileForm(FlaskForm):
    real_name = StringField("真实名字")
    email = StringField('邮箱', validators = [Required(), Email()])
    password = PasswordField('密码(不填写保持不变)')
    phone = StringField('电话号码')
    workyears = IntegerField("工作年限")
    resume_url = StringField('简历地址')
    submit = SubmitField('提交')
    
    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13', '15', '18') and len(phone) != 11:
            raise ValidationError('请输入有效的手机号')

    def updated_profile(self, user):
        user.real_name = self.real_name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        user.phone = self.phone.data
        user.work_years = self.workyears.data
        user.resume_url = self.resume_url.data
        db.session.add(user)
        db.session.commit()




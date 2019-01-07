from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from  werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Base(db.Model):

    #不生成数据库
    __abstract__ = True

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, 
                        default = datetime.utcnow, 
                        onupdate = datetime.utcnow)



class User(Base):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique = True, index = True, nullable = False) 
    email = db.Column(db.String(64), unique = True, index = True, nullable = False)
    _password = db.Column('password', db.String(256), nullable = False)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    resume = db.relationship('Resume', uselist = False)
    #collect_jobs = 
    upload_resume_url = db.Column(db.String(64))

    def __repr__(self):
        return '<User:{}>'.format(self.username)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)
   
    def check_password(self, pwd):
        return check_password_hash(self._password, pwd)
    
    @property
    def is_admin(self):
        return self.role == ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == ROLE_COMPANY

    @property
    def is_user(self):
        return self.role == ROLE_USER

class Resume(Base):
    __tablename__ = 'resume'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', uselist = False)
    job_experiences = db.relationship('JobExperience')
    edu_experiences = db.relationship('EduExperience')
    project_experiences = db.relationship('ProjectExperience')

class Experience(Base):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    begin_at = db.Column(db.DateTime)
    end_at = db.Column(db.DateTime)

    description = db.Column(db.String(1024))

class JobExperience(Experience):
    __tablename__ = 'job_experience'

    company = db.Column(db.String(64), nullable = False)
    city = db.Column(db.String(32), nullable = False)
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))
    resume = db.relationship('Resume', uselist = False)

class EduExperience(Experience):
    __tablename__ = 'edu_experience'

    school = db.Column(db.String(32), nullable = False)
    degree = db.Column(db.String(16), nullable = False)
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))
    resume = db.relationship('Resume', uselist = False)

class ProjectExperience(Experience):
    __tablename__ = 'projece_experience'
    name = db.Column(db.String(64), nullable = False)
    role = db.Column(db.String(32))
    technologys = db.Column(db.String(64))
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))
    resume = db.relationship('Resume', uselist = False)




class Company(Base):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False, index = True, unique = True)
    slug = db.Column(db.String(24), nullable = False, index = True, unique = True)
    logo = db.Column(db.String(64), nullable = False)
    site = db.Column(db.String(64), nullable = False)
    contact = db.Column(db.String(24), nullable = False)
    email = db.Column(db.String(24), nullable = False)
    location = db.Column(db.String(24), nullable = False)

    description = db.Column(db.String(100))
    about = db.Column(db.String(1024))
    tags = db.Column(db.String(128))
    stack = db.Column(db.String(128))
    team_introduction = db.Column(db.String(256))
    welfares = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'SET NULL'))
    user = db.relationship('User', uselist = False, backref = db.backref('company', uselist = False))


    def __repr__(self):
        return '<Company {}>'.format(self.name)

class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(24))
    salary_low = db.Column(db.Integer, nullable = False)
    salary_high = db.Column(db.Integer, nullable = False)
    location = db.Column(db.String(24))
    tags = db.Column(db.String(128))
    experice_requirement = db.Column(db.String(32))
    degree_requirement = db.Column(db.String(32))
    is_fulltime = db.Column(db.Boolean, default = True)

    is_open = db.Column(db.Boolean, default = True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete = 'CASCADE'))
    company = db.relationship('Company', uselist = False)
    views_count = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return '<Job {}>'.format(self.name)






from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

#db = SQLAlchemy(app)
db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)


class User(Base):
    __tablename__ = 'user'
    
    ROLE_USER = 10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique = True, index = True, nullable = False)
    email = db.Column(db.String(64), unique = True, index = True, nullable = False)
    #明确列名为password
    _password = db.Column('password', db.String(512), nullable = False)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    job = db.Column(db.String(64))
    publish_courses = db.relationship('Course')


    def __repr__(self):
        return '<User: {}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, ori_password):
        
        self._password = ori_password
        #self._password = generate_password_hash(ori_password)

    def check_password(self, password):
        return True
        #return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == ROLE_ADMIN

    @property
    def is_staff(self):
        return self.role == ROLE_STAFF

class Course(Base):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), unique = True, index = True, nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'))
    author = db.relationship('User', uselist = False)
    


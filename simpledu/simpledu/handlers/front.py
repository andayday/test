from flask import Blueprint, render_template
from simpledu.models import Course
from simpledu.models import User

front = Blueprint('front', __name__)

@front.route('/')
def index():
    userinfo = User.query.get(username = "admin")
    print("userinfo : ", userinfo)
    courses = Course.query.all()
    return render_template('index.html', courses = courses)

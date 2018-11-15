from flask import abort
from flask_login import current_user
from functools import wraps
from simpledu.models import User

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("test 111111111111")
            if not current_user.is_authenticated or current_user.role < role:
                print("test 222222222")
                abort(404)
            return func(*args, **kwargs)
        return wrapper
    return decorator

staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)


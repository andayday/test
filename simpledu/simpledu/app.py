from flask import Flask , render_template
from simpledu.config import configs
from simpledu.models import db, Course

def register_blueprint(app):
    from .handlers import front, course, admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)

def create_app(config):
    """
    可以根据传入的config名称，加载不同的配置
    """

    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprint(app)

    return app



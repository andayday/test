from flask import Blueprint, render_template, request
from simpledu.decorators import admin_required

admin = Blueprint('admin', __name__, url_prefix = '/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/users')
def users():
    page = request.args.get('page', default = 1, type = int)
    pagination = User.query.paginate(
            page = page,
            per_page = current_app.config['ADMIN_PER_PAGE'],
            error_out = False,
            )
    return render_template('admin/users.html', pagination = pagination)
    


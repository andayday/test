from flask import Blueprint, render_template, request, current_app, url_for, flash, redirect
from simpledu.decorators import admin_required
from simpledu.models import User, db
from simpledu.forms import RegisterForm

admin = Blueprint('admin', __name__, url_prefix = '/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/users')
@admin_required
def users():
    page = request.args.get('page', default = 1, type = int)
    pagination = User.query.paginate(
            page = page,
            per_page = current_app.config['INDEX_PER_PAGE'],
            error_out = False,
            )
    return render_template('admin/users.html', pagination = pagination)
   
@admin.route('/users/create', methods = ['GET', 'POST'])
@admin_required
def create_user():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('create success', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_user.html', form = form)


@admin.route('/users/<int:user_id>/edit', methods = ['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = RegisterForm(obj = user)
    if form.is_submitted():
        form.populate_obj(user)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash('user or email already exist', 'error')
        else:
            flash('update success', 'success')
            return redirect(url_for('admin.users'))

    return render_template('admin/edit_user.html', form = form, user = user)


@admin.route('/users/<int:user_id>/delete', methods = ['GET', 'POST'])
@admin_required
def delete_user(user_id):
    pass



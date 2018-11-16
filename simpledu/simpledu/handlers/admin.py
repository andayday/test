from flask import Blueprint, render_template, request, current_app, url_for, flash, redirect
from simpledu.decorators import admin_required
from simpledu.models import User, db, Course
from simpledu.forms import RegisterForm, CourseForm

admin = Blueprint('admin', __name__, url_prefix = '/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

@admin.route('/courses')
@admin_required
def courses():
    page = request.args.get('page', default = 1, type = int)
    pagination = Course.query.paginate(
            page = page,
            per_page = current_app.config['INDEX_PER_PAGE'],
            error_out = False,
            )
    return render_template('admin/courses.html', pagination = pagination)


@admin.route('/courses/create', methods = ['GET', 'POST'])
@admin_required
def create_course():
    form = CourseForm()
    if form.validate_on_submit():
        form.create_course()
        flash('create success', 'success')
        return redirect(url_for('admin.course'))
    return render_template('admin/create_course.html', form = form)


@admin.route('/courses/<int:course_id>/edit', methods = ['GET', 'POST'])
@admin_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj = course)
    if form.is_submitted():
        form.populate_obj(course)
        db.session.add(course)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash('coursealready exist', 'error')
        else:
            flash('update success', 'success')
            return redirect(url_for('admin.courses'))

    return render_template('admin/edit_course.html', form = form, course = course)



@admin.route('/courses/<int:course_id>/delete', methods = ['GET', 'POST'])
@admin_required
def delete_course(course_id):
    pass



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
    if current_user.id == user_id:
        flash('user do not delete self', 'error')
        return redirect(url_for('admin.users'))

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('user have delete', 'success')
    return redirect(url_for('admin.users'))


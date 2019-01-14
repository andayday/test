from flask import Blueprint, flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from jobplus.forms import CompanyProfileForm
from jobplus.models import User

company = Blueprint('company', __name__, url_prefix = '/company')


@company.route('/')
def index():
    page = request.args.get('page', 1, type = int)
    pagination = User.query.filter(User.role == User.ROLE_COMPANY).order_by(User.created_at.desc()).paginate(
            page = page,
            per_page = current_app.config['INDEX_PER_PAGE'],
            error_out = False,
            )
    return render_template('company/index.html', pagination = pagination, active = 'company')
        

@company.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    form = CompanyProfileForm()
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('个人信息更新成功', 'success')
        return redirect(url_for('front.index'))

    return render_template('company/profile.html', form = form)




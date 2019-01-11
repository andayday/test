from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from jobplus.forms import UserProfileFrom

user = Blueprint('user', __name__, url_prefix = '/user')

@user.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('个人信息更新成功', 'success')
        return redirect(url_for('front.index'))

    return render_template('user/profile.html', form = form)



from flask import Blueprint, redirect, url_for, request, flash, render_template
from flask_login import current_user, login_user, logout_user, login_required

from .forms import LoginForm
from .models import User
from project import db

auth_bp = Blueprint(
    'auth_bp',
    __name__,
    template_folder='templates',
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth_bp.main'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get('next')
                flash('Ви увійшли до акаунту.', 'success')
                return redirect(url_for('car_bp.download_sketch')) if not next_page else redirect(next_page)
            else:
                flash('Неправильні дані, будь ласка, перевірте логін та пароль.', 'failed')
    return render_template('auth/login.html', title='Вхід', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/')
@login_required
def main():
    return "Works!"

# @auth_bp.route('/creator')
# def creator():
#     from .models import UserRoleEnum
#     u1 = User(first_name="Artem", second_name="Lebedev", role=UserRoleEnum.teacher, email="art.lebedev2020@gmail.com")
#     u1.set_password("123")
#     db.session.add(u1)
#     db.session.commit()
#     return "Created!"

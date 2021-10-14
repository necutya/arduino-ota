import enum

from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from project import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserRoleEnum(enum.Enum):
    teacher = 'Вчитель'
    student = 'Студент'


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    second_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    group = db.Column(db.String(5), unique=False, nullable=True)
    role = db.Column(db.Enum(UserRoleEnum), default=UserRoleEnum.student, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def is_admin(self):
        return self.role == User.ROLES['admin']

    def allowed(self, access_level):
        return self.role >= access_level

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"{self.first_name} {self.second_name}"

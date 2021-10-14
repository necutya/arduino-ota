import wtforms
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = wtforms.StringField('Пошта', validators=[DataRequired(), Email()])
    password = wtforms.PasswordField('Пароль', validators=[DataRequired()])
    remember_me = wtforms.BooleanField("Запам'ятати мене")
    submit = wtforms.SubmitField('Увійти')

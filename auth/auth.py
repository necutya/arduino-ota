from flask import Blueprint, render_template

auth_bp = Blueprint(
    'products_bp',
    __name__,
    template_folder='templates',
)


@auth_bp.route('/')
def view():
    return "Works!"

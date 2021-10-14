import os

from flask import Blueprint, redirect, url_for, request, flash, render_template
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename

from .forms import CarSketchForm
from .tasks import process_arduino_sketch

cars_bp = Blueprint(
    'cars_bp',
    __name__,
    template_folder='templates',
)

@cars_bp.route('/download-sketch', methods=["GET", "POST"])
@login_required
def download_sketch():
    form = CarSketchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            f = form.sketch.data
            filename = f"user_{current_user.id}.ino"
            bin_path = os.path.join(f"{cars_bp.root_path}", "sketches", "bin")
            filepath = os.path.join(f"{cars_bp.root_path}/sketches", filename)
            f.save(filepath)
            process_arduino_sketch(filepath, bin_path)
            flash('Файл оброблюється', 'success')
        else:
            flash('Тільки файли з розшренням .ino!', 'failed')
    return render_template('cars/download_sketch.html', title='Вхід', form=form)

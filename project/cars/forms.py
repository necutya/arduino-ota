import wtforms
from flask_wtf import FlaskForm, file


class CarSketchForm(FlaskForm):
    sketch = file.FileField(
        'Файл скетчу',
        validators=[
            file.FileRequired(),
            file.FileAllowed(['ino', ], 'Тільки файли з розшренням .ino!')
        ]
    )
    submit = wtforms.SubmitField('Відправити')

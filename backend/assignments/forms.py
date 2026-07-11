from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired


class AssignmentForm(FlaskForm):

    asset = SelectField(
        "Asset",
        coerce=int,
        validators=[DataRequired()]
    )

    employee = SelectField(
        "Employee",
        coerce=int,
        validators=[DataRequired()]
    )

    assigned_date = DateField(
        "Assigned Date",
        validators=[DataRequired()]
    )

    submit = SubmitField("Assign Asset")
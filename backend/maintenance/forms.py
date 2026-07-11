from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class MaintenanceForm(FlaskForm):

    asset = SelectField(
        "Asset",
        coerce=int,
        validators=[DataRequired()]
    )

    issue = StringField(
        "Issue",
        validators=[DataRequired()]
    )

    submit = SubmitField("Send For Maintenance")
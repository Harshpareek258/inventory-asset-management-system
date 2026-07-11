from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email


class EmployeeForm(FlaskForm):

    employee_id = StringField(
        "Employee ID",
        validators=[DataRequired()]
    )

    full_name = StringField(
        "Full Name",
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",
        validators=[Email()]
    )

    phone = StringField("Phone")

    department = SelectField(
        "Department",
        choices=[
            ("IT","IT"),
            ("HR","HR"),
            ("Finance","Finance"),
            ("Admin","Admin")
        ]
    )

    designation = StringField("Designation")

    status = SelectField(
        "Status",
        choices=[
            ("Active","Active"),
            ("Inactive","Inactive")
        ]
    )

    submit = SubmitField("Save Employee")
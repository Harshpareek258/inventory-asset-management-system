from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    SubmitField
)
from wtforms.validators import DataRequired


class AssetForm(FlaskForm):

    asset_name = StringField(
        "Asset Name",
        validators=[DataRequired()]
    )

    asset_code = StringField(
        "Asset Code",
        validators=[DataRequired()]
    )

    category = SelectField(
        "Category",
        choices=[
            ("Laptop", "Laptop"),
            ("Desktop", "Desktop"),
            ("Monitor", "Monitor"),
            ("Printer", "Printer"),
            ("Accessory", "Accessory"),
            ("Network", "Network"),
        ]
    )

    status = SelectField(
        "Status",
        choices=[
            ("Available", "Available"),
            ("Assigned", "Assigned"),
            ("Maintenance", "Maintenance")
        ]
    )

    purchase_date = DateField(
        "Purchase Date",
        format="%Y-%m-%d"
    )

    submit = SubmitField("Save Asset")
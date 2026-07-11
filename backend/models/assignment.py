from backend.extensions import db


class Assignment(db.Model):

    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)

    asset_id = db.Column(
        db.Integer,
        db.ForeignKey("assets.id"),
        nullable=False
    )

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    assigned_date = db.Column(
        db.Date,
        nullable=False
    )

    returned_date = db.Column(
        db.Date
    )

    status = db.Column(
        db.String(30),
        default="Assigned"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    asset = db.relationship("Asset")

    employee = db.relationship("Employee")
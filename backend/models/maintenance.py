from backend.extensions import db


class Maintenance(db.Model):

    __tablename__ = "maintenance"

    id = db.Column(db.Integer, primary_key=True)

    asset_id = db.Column(
        db.Integer,
        db.ForeignKey("assets.id")
    )

    issue = db.Column(db.String(250))

    status = db.Column(
        db.String(30),
        default="Pending"
    )

    reported_date = db.Column(
        db.Date
    )

    resolved_date = db.Column(
        db.Date
    )

    asset = db.relationship("Asset")
from backend.extensions import db


class Asset(db.Model):

    __tablename__ = "assets"

    id = db.Column(db.Integer, primary_key=True)

    asset_name = db.Column(db.String(120), nullable=False)

    asset_code = db.Column(db.String(60), unique=True)

    category = db.Column(db.String(80))

    status = db.Column(db.String(40))

    purchase_date = db.Column(db.Date)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
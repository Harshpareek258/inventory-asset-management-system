from datetime import date

from flask import render_template, redirect, url_for, flash

from backend.maintenance import maintenance_bp
from backend.maintenance.forms import MaintenanceForm
from backend.extensions import db
from backend.models.asset import Asset
from backend.models.maintenance import Maintenance


@maintenance_bp.route("/")
def list_maintenance():

    records = Maintenance.query.order_by(
        Maintenance.id.desc()
    ).all()

    return render_template(
        "maintenance.html",
        records=records,
        active_page="maintenance"
    )


@maintenance_bp.route("/add", methods=["GET", "POST"])
def add_maintenance():

    form = MaintenanceForm()

    form.asset.choices = [
        (a.id, f"{a.asset_code} - {a.asset_name}")
        for a in Asset.query.filter_by(status="Available").all()
    ]

    if form.validate_on_submit():

        asset = Asset.query.get(form.asset.data)
        asset.status = "Under Maintenance"

        maintenance = Maintenance(
            asset_id=form.asset.data,
            issue=form.issue.data,
            reported_date=date.today(),
            status="Pending"
        )

        db.session.add(maintenance)
        db.session.commit()

        flash("Asset sent for maintenance successfully!", "success")

        return redirect(url_for("maintenance.list_maintenance"))

    return render_template(
        "maintenance_form.html",
        form=form,
        active_page="maintenance"
    )


@maintenance_bp.route("/complete/<int:id>")
def complete_maintenance(id):

    record = Maintenance.query.get_or_404(id)

    record.status = "Completed"
    record.resolved_date = date.today()

    asset = Asset.query.get(record.asset_id)
    asset.status = "Available"

    db.session.commit()

    flash("Maintenance completed successfully!", "success")

    return redirect(url_for("maintenance.list_maintenance"))
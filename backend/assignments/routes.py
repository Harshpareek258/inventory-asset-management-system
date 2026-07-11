from flask import render_template, redirect, url_for, flash
from backend.assignments import assignments_bp
from backend.assignments.forms import AssignmentForm
from backend.extensions import db
from backend.models.assignment import Assignment
from backend.models.asset import Asset
from backend.models.employee import Employee


@assignments_bp.route("/")
def list_assignments():

    assignments = Assignment.query.order_by(
        Assignment.id.desc()
    ).all()

    return render_template(
    "assignments.html",
    assignments=assignments,
    active_page="assignments"
)


@assignments_bp.route("/add", methods=["GET", "POST"])
def add_assignment():

    form = AssignmentForm()

    form.asset.choices = [
        (a.id, f"{a.asset_code} - {a.asset_name}")
        for a in Asset.query.filter_by(status="Available").all()
    ]

    form.employee.choices = [
        (e.id, f"{e.employee_id} - {e.full_name}")
        for e in Employee.query.all()
    ]

    if form.validate_on_submit():

        assignment = Assignment(
            asset_id=form.asset.data,
            employee_id=form.employee.data,
            assigned_date=form.assigned_date.data
        )

        asset = Asset.query.get(form.asset.data)
        asset.status = "Assigned"

        db.session.add(assignment)
        db.session.commit()

        flash("Asset Assigned Successfully!", "success")

        return redirect(url_for("assignments.list_assignments"))

    return render_template(
        "assignment_form.html",
        form=form
    )


@assignments_bp.route("/return/<int:id>")
def return_asset(id):

    assignment = Assignment.query.get_or_404(id)

    assignment.status = "Returned"

    assignment.returned_date = db.func.current_date()

    asset = Asset.query.get(assignment.asset_id)

    asset.status = "Available"

    db.session.commit()

    flash("Asset Returned Successfully!", "success")

    return redirect(url_for("assignments.list_assignments"))
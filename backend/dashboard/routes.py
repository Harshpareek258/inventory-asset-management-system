from flask import render_template
from backend.dashboard import dashboard_bp
from backend.models.asset import Asset
from backend.models.employee import Employee
from backend.models.assignment import Assignment
from backend.models.maintenance import Maintenance


@dashboard_bp.route("/")
@dashboard_bp.route("/dashboard")
def index():

    # Dashboard Statistics
    stats = {
        "total_assets": Asset.query.count(),
        "assigned_assets": Asset.query.filter_by(status="Assigned").count(),
        "available_assets": Asset.query.filter_by(status="Available").count(),
        "employees": Employee.query.count(),
        "maintenance": Maintenance.query.filter_by(status="Pending").count(),
        "assignments": Assignment.query.count()
    }

    # Latest 5 Assets
    recent_assets = Asset.query.order_by(
        Asset.created_at.desc()
    ).limit(5).all()

    # Latest 5 Assignments
    recent_assignments = Assignment.query.order_by(
        Assignment.id.desc()
    ).limit(5).all()

    # Temporary Activities
    recent_activities = [
        {
            "activity": "System Started",
            "description": "Inventory Management System is running",
            "user": "Admin",
            "timestamp": "-"
        }
    ]

    return render_template(
        "dashboard.html",
        stats=stats,
        recent_assets=recent_assets,
        recent_assignments=recent_assignments,
        recent_activities=recent_activities,
        active_page="dashboard"
    )
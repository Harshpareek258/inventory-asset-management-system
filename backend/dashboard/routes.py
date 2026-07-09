"""
Dashboard Routes
-----------------
Defines the view functions (routes) for the Dashboard module.

NOTE: This module currently uses static sample data only.
No database/backend logic has been wired in yet — that will be
handled once the Assets, Employees, Assignments, and Maintenance
modules are implemented.
"""

from flask import render_template
from backend.dashboard import dashboard_bp


@dashboard_bp.route("/")
@dashboard_bp.route("/dashboard")
def index():
    """
    Renders the main enterprise dashboard page.
    Displays summary statistic cards, a recent assets table,
    and a recent activities table using static sample data.
    """

    # ---------------------------------------------------------
    # Static Sample Data (Placeholder — to be replaced later)
    # ---------------------------------------------------------

    stats = {
        "total_assets": 1284,
        "assigned_assets": 812,
        "available_assets": 472,
        "employees": 156
    }

    recent_assets = [
        {
            "asset_id": "AST-1042",
            "name": "Dell Latitude 5440 Laptop",
            "category": "Laptop",
            "status": "Assigned",
            "assigned_to": "Rohit Sharma",
            "date_added": "2026-07-01"
        },
        {
            "asset_id": "AST-1041",
            "name": "HP LaserJet Pro M404",
            "category": "Printer",
            "status": "Available",
            "assigned_to": "-",
            "date_added": "2026-06-29"
        },
        {
            "asset_id": "AST-1040",
            "name": "Logitech MX Master 3S",
            "category": "Accessory",
            "status": "Assigned",
            "assigned_to": "Anjali Verma",
            "date_added": "2026-06-27"
        },
        {
            "asset_id": "AST-1039",
            "name": "Apple MacBook Pro 14\"",
            "category": "Laptop",
            "status": "Under Maintenance",
            "assigned_to": "Karan Mehta",
            "date_added": "2026-06-25"
        },
        {
            "asset_id": "AST-1038",
            "name": "Dell UltraSharp 27\" Monitor",
            "category": "Monitor",
            "status": "Available",
            "assigned_to": "-",
            "date_added": "2026-06-22"
        }
    ]

    recent_activities = [
        {
            "activity": "Asset Assigned",
            "description": "AST-1042 assigned to Rohit Sharma",
            "user": "Admin",
            "timestamp": "2026-07-08 10:32 AM"
        },
        {
            "activity": "Asset Added",
            "description": "New asset HP LaserJet Pro M404 added to inventory",
            "user": "Admin",
            "timestamp": "2026-07-07 04:15 PM"
        },
        {
            "activity": "Maintenance Logged",
            "description": "MacBook Pro 14\" sent for screen repair",
            "user": "IT Support",
            "timestamp": "2026-07-06 11:48 AM"
        },
        {
            "activity": "Employee Added",
            "description": "New employee Anjali Verma onboarded",
            "user": "HR Admin",
            "timestamp": "2026-07-05 09:20 AM"
        },
        {
            "activity": "Asset Returned",
            "description": "AST-1030 returned by Suresh Nair",
            "user": "Admin",
            "timestamp": "2026-07-04 02:10 PM"
        }
    ]

    return render_template(
        "dashboard.html",
        stats=stats,
        recent_assets=recent_assets,
        recent_activities=recent_activities,
        active_page="dashboard"
    )
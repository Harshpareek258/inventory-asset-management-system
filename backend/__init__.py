from flask import Flask, redirect, url_for

from config import Config
from backend.extensions import db, migrate, login_manager


def create_app(config_class=Config):

    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    # -----------------------------
    # Load Configuration
    # -----------------------------
    app.config.from_object(config_class)

    # -----------------------------
    # Initialize Extensions
    # -----------------------------
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to continue."
    login_manager.login_message_category = "warning"

    # -----------------------------
    # Import Models
    # -----------------------------
    from backend.models.user import User
    from backend.models.asset import Asset
    from backend.models.employee import Employee
    from backend.models.assignment import Assignment
    from backend.models.maintenance import Maintenance

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # -----------------------------
    # Register Blueprints
    # -----------------------------
    from backend.auth import auth_bp
    from backend.dashboard import dashboard_bp
    from backend.assets import assets_bp
    from backend.employees import employees_bp
    from backend.assignments import assignments_bp
    from backend.maintenance import maintenance_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(assets_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(assignments_bp)
    app.register_blueprint(maintenance_bp)

    # -----------------------------
    # Home Route
    # -----------------------------
    @app.route("/")
    def home():
        return redirect(url_for("dashboard.index"))

    return app
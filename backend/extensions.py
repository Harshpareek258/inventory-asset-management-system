"""
Flask Extensions
------------------
Centralized initialization of Flask extensions so they can be
imported without causing circular import issues across the
application factory and blueprint modules.

Extensions are instantiated here (unbound) and initialized against
the Flask app instance later inside create_app() (backend/__init__.py).
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# ---------------------------------------------------------
# Database ORM
# ---------------------------------------------------------
db = SQLAlchemy()

# ---------------------------------------------------------
# Database Migrations
# ---------------------------------------------------------
migrate = Migrate()

# ---------------------------------------------------------
# Login / Session Management
# ---------------------------------------------------------
login_manager = LoginManager()

# Name of the view function Flask-Login redirects to when an
# unauthenticated user attempts to access a @login_required route.
login_manager.login_view = "auth.login"
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "warning"
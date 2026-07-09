"""
User Model
------------
Defines the User table used for authentication and role-based
access control (Admin / Employee).

Passwords are never stored in plain text — Werkzeug's
generate_password_hash / check_password_hash utilities are used
to securely hash and verify credentials.
"""

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from backend.extensions import db


class User(UserMixin, db.Model):
    """
    Represents an application user (Admin or Employee).

    UserMixin (from Flask-Login) provides default implementations
    for is_authenticated, is_active, is_anonymous, and get_id().
    """

    __tablename__ = "users"

    # ---------------------------------------------------------
    # Role Constants
    # ---------------------------------------------------------
    ROLE_ADMIN = "admin"
    ROLE_EMPLOYEE = "employee"

    VALID_ROLES = (ROLE_ADMIN, ROLE_EMPLOYEE)

    # ---------------------------------------------------------
    # Columns
    # ---------------------------------------------------------
    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(150), nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False, index=True)

    password_hash = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), nullable=False, default=ROLE_EMPLOYEE)

    is_active_account = db.Column(db.Boolean, default=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # ---------------------------------------------------------
    # Password Helpers
    # ---------------------------------------------------------
    def set_password(self, raw_password):
        """Hashes and stores the given plain-text password."""
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        """Verifies a plain-text password against the stored hash."""
        return check_password_hash(self.password_hash, raw_password)

    # ---------------------------------------------------------
    # Role Helpers
    # ---------------------------------------------------------
    @property
    def is_admin(self):
        """Returns True if the user has the Admin role."""
        return self.role == self.ROLE_ADMIN

    @property
    def is_employee(self):
        """Returns True if the user has the Employee role."""
        return self.role == self.ROLE_EMPLOYEE

    # ---------------------------------------------------------
    # Flask-Login Overrides
    # ---------------------------------------------------------
    @property
    def is_active(self):
        """
        Overrides UserMixin's default is_active property so that
        deactivated accounts cannot log in or maintain a session.
        """
        return self.is_active_account

    # ---------------------------------------------------------
    # Representation
    # ---------------------------------------------------------
    def __repr__(self):
        return f"<User id={self.id} email={self.email} role={self.role}>"
    
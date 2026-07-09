"""
Authentication Routes
------------------------
Defines the view functions (routes) for the Authentication module:
    - Login  (GET / POST)
    - Logout (GET)

Uses Flask-Login for session management and Werkzeug (via the
User model) for secure password verification.
"""

from urllib.parse import urlparse

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from backend.auth import auth_bp
from backend.auth.forms import LoginForm
from backend.models.user import User


def _is_safe_redirect_url(target):
    """
    Ensures a 'next' redirect target is a relative, same-site URL
    to prevent open-redirect vulnerabilities.
    """
    if not target:
        return False
    parsed = urlparse(target)
    return not parsed.netloc and not parsed.scheme


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles user login.

    - If the user is already authenticated, redirects to the dashboard.
    - On valid POST submission, verifies credentials and starts a
      session using Flask-Login.
    - On failure, re-renders the form with a flashed error message.
    """

    # Redirect already-authenticated users straight to the dashboard
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            flash("Invalid email or password. Please try again.", "danger")
            return render_template("auth/login.html", form=form)

        if not user.is_active:
            flash("Your account has been deactivated. Please contact an administrator.", "warning")
            return render_template("auth/login.html", form=form)

        # Log the user in and start the session
        login_user(user, remember=form.remember_me.data)
        flash(f"Welcome back, {user.full_name}!", "success")

        # Honor a safe 'next' redirect target if one was provided
        next_page = request.args.get("next")
        if next_page and _is_safe_redirect_url(next_page):
            return redirect(next_page)

        return redirect(url_for("dashboard.index"))

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    """
    Logs out the current user, clears the session, and redirects
    back to the login page with a confirmation message.
    """
    logout_user()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for("auth.login"))
from flask import render_template, redirect, url_for, flash
from backend.employees import employees_bp
from backend.employees.forms import EmployeeForm
from backend.extensions import db
from backend.models.employee import Employee


# ==========================
# View Employees
# ==========================
@employees_bp.route("/")
def list_employees():

    employees = Employee.query.order_by(Employee.id.desc()).all()

    return render_template(
    "employees.html",
    employees=employees,
    active_page="employees"
)


# ==========================
# Add Employee
# ==========================
@employees_bp.route("/add", methods=["GET", "POST"])
def add_employee():

    form = EmployeeForm()

    if form.validate_on_submit():

        employee = Employee(
            employee_id=form.employee_id.data,
            full_name=form.full_name.data,
            email=form.email.data,
            phone=form.phone.data,
            department=form.department.data,
            designation=form.designation.data,
            status=form.status.data
        )

        db.session.add(employee)
        db.session.commit()

        flash("Employee Added Successfully!", "success")

        return redirect(url_for("employees.list_employees"))

    return render_template(
        "employee_form.html",
        form=form,
        title="Add Employee"
    )


# ==========================
# Edit Employee
# ==========================
@employees_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    employee = Employee.query.get_or_404(id)

    form = EmployeeForm(obj=employee)

    if form.validate_on_submit():

        employee.employee_id = form.employee_id.data
        employee.full_name = form.full_name.data
        employee.email = form.email.data
        employee.phone = form.phone.data
        employee.department = form.department.data
        employee.designation = form.designation.data
        employee.status = form.status.data

        db.session.commit()

        flash("Employee Updated Successfully!", "success")

        return redirect(url_for("employees.list_employees"))

    return render_template(
        "employee_form.html",
        form=form,
        title="Edit Employee"
    )


# ==========================
# Delete Employee
# ==========================
@employees_bp.route("/delete/<int:id>")
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)

    db.session.commit()

    flash("Employee Deleted Successfully!", "success")

    return redirect(url_for("employees.list_employees"))
from backend.extensions import db


class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(db.String(20), unique=True, nullable=False)

    full_name = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(120), unique=True)

    phone = db.Column(db.String(20))

    department = db.Column(db.String(80))

    designation = db.Column(db.String(80))

    status = db.Column(
        db.String(30),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Employee {self.full_name}>"
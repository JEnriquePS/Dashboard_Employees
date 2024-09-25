from app.employees.domain.employee import Employee
from app.infrastructure.db.sqlalchemy_connector import db

def create_employee(nombre, edad, ciudad, salario):
    employee = Employee(nombre, edad, ciudad, salario)
    db.session.add(employee)
    db.session.commit()
    return employee
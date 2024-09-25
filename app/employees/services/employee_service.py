from app.employees.commands.create_employee import create_employee
from app.employees.queries.get_employees import get_all_employees

class EmployeeService:
    def add_employee(self, nombre, edad, ciudad, salario):
        create_employee(nombre, edad, ciudad, salario)

    def list_employees(self):
        return get_all_employees()
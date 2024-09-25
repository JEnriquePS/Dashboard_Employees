from app.employees.domain.employee import Employee

def get_all_employees():
    return Employee.query.all()
from main import create_app
from employees.domain.employee import Employee
from infrastructure.db.sqlalchemy_connector import db

app = create_app()

example_employees = [
    Employee(nombre='Juan Pérez', edad=22, ciudad='Lima', salario=1500.50),
    Employee(nombre='Ana García', edad=25, ciudad='Arequipa', salario=1800.00),
    Employee(nombre='Carlos Fernández', edad=27, ciudad='Cusco', salario=2000.75),
    Employee(nombre='Laura Gómez', edad=23, ciudad='Trujillo', salario=1600.25),
    Employee(nombre='Miguel López', edad=21, ciudad='Chiclayo', salario=1400.00),
    Employee(nombre='Lucía Martínez', edad=26, ciudad='Iquitos', salario=1900.10),
    Employee(nombre='Pedro Sánchez', edad=29, ciudad='Piura', salario=2100.90),
    Employee(nombre='Sofía Díaz', edad=20, ciudad='Tacna', salario=1350.30),
    Employee(nombre='David Hernández', edad=28, ciudad='Huancayo', salario=2050.60),
    Employee(nombre='María Jiménez', edad=30, ciudad='Puno', salario=2200.75),
    Employee(nombre='Luis Torres', edad=31, ciudad='Lima', salario=2400.25),
    Employee(nombre='Patricia Vega', edad=32, ciudad='Arequipa', salario=2600.10),
    Employee(nombre='Fernando Castro', edad=33, ciudad='Cusco', salario=2800.85),
    Employee(nombre='Gloria Rojas', edad=24, ciudad='Trujillo', salario=1700.00),
    Employee(nombre='Manuel Ruiz', edad=34, ciudad='Chiclayo', salario=2900.60),
    Employee(nombre='Carmen Flores', edad=35, ciudad='Iquitos', salario=3000.75),
    Employee(nombre='Rafael Paredes', edad=36, ciudad='Piura', salario=3200.45),
    Employee(nombre='Adriana Villegas', edad=22, ciudad='Tacna', salario=1500.90),
    Employee(nombre='Felipe Gutiérrez', edad=27, ciudad='Huancayo', salario=2000.30),
    Employee(nombre='Teresa Navarro', edad=40, ciudad='Puno', salario=4000.20),
            ]

with app.app_context():
    db.create_all()
    if not Employee.query.first():
        # Insertar los empleados de ejemplo en la base de datos
        db.session.bulk_save_objects(example_employees)
        db.session.commit()
        print("Base inicializada y datos insertados correctamente.")
    else:
        print("Base inicializada")

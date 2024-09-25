from flask_sqlalchemy import SQLAlchemy

def database_mock():
    from app.employees.domain.employee import Employee
    example_employees = [
        Employee(nombre='Juan Pérez', edad=22, ciudad='Lima', salario=1500.0),
        Employee(nombre='Ana García', edad=25, ciudad='Arequipa', salario=1800.00),
        Employee(nombre='Carlos Fernández', edad=27, ciudad='Cusco', salario=2000.0),
        Employee(nombre='Laura Gómez', edad=23, ciudad='Trujillo', salario=1600.0),
        Employee(nombre='Miguel López', edad=21, ciudad='Chiclayo', salario=1400.00),
        Employee(nombre='Lucía Martínez', edad=26, ciudad='Iquitos', salario=1900.0),
        Employee(nombre='Pedro Sánchez', edad=29, ciudad='Piura', salario=2100.0),
        Employee(nombre='Sofía Díaz', edad=20, ciudad='Tacna', salario=1350.0),
        Employee(nombre='David Hernández', edad=28, ciudad='Huancayo', salario=2050.0),
        Employee(nombre='María Jiménez', edad=30, ciudad='Lima', salario=2200.0),
        Employee(nombre='Luis Torres', edad=31, ciudad='Lima', salario=2400.0),
        Employee(nombre='Patricia Vega', edad=32, ciudad='Arequipa', salario=2600.0),
        Employee(nombre='Fernando Castro', edad=33, ciudad='Cusco', salario=2800.0),
        Employee(nombre='Gloria Rojas', edad=24, ciudad='Trujillo', salario=1700.00),
        Employee(nombre='Manuel Ruiz', edad=34, ciudad='Lima', salario=2900.0),
        Employee(nombre='Carmen Flores', edad=35, ciudad='Iquitos', salario=3000.0),
        Employee(nombre='Rafael Paredes', edad=36, ciudad='Lima', salario=3200.0),
        Employee(nombre='Adriana Villegas', edad=22, ciudad='Tacna', salario=1500.0),
        Employee(nombre='Felipe Gutiérrez', edad=27, ciudad='Lima', salario=2000.0),
        Employee(nombre='Teresa Navarro', edad=40, ciudad='Puno', salario=4000.0),
    ]
    return example_employees

db = SQLAlchemy()

def init_db(app):
    from app.employees.domain.employee import Employee
    """Inicializa la base de datos"""
    db.init_app(app)
    with app.app_context():
        db.create_all()
        if not Employee.query.first():
            # Insertar los empleados de ejemplo en la base de datos
            db.session.bulk_save_objects(database_mock())
            db.session.commit()
            print("Base inicializada y datos insertados correctamente.")
        else:
            print("Base inicializada")



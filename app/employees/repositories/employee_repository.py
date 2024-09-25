from app.infrastructure.db.mysql_connector import get_mysql_connection
from app.infrastructure.db.sqlite_connector import get_sqlite_connection
from app.employees.domain.employee import Employee
from app.config import DB_CONFIG



class EmployeeRepository:
    def __init__(self):
        self.db_type =  DB_CONFIG.get('DB_TYPE', 'sqlite')

    def _get_connection(self):
        if self.db_type == 'mysql':
            return get_mysql_connection()
        elif self.db_type == 'sqlite':
            return get_sqlite_connection()
        else:
            raise ValueError("Tipo de base de datos no soportado")

    def save(self, employee: Employee):
        connection = self._get_connection()
        if connection:
            cursor = connection.cursor()
            if self.db_type == 'mysql':
                query = """
                INSERT INTO empleado (nombre, edad, ciudad, salario)
                VALUES (%s, %s, %s, %s);
                """
                cursor.execute(query, (employee.nombre, employee.edad, employee.ciudad, employee.salario))
            elif self.db_type == 'sqlite':
                query = """
                INSERT INTO empleado (nombre, edad, ciudad, salario)
                VALUES (?, ?, ?, ?);
                """
                cursor.execute(query, (employee.nombre, employee.edad, employee.ciudad, employee.salario))

            connection.commit()
            cursor.close()
            connection.close()

    def get_all(self):
        connection = self._get_connection()
        if connection:
            cursor = connection.cursor()
            if self.db_type == 'mysql':
                query = "SELECT * FROM empleado;"
                cursor.execute(query)
                results = cursor.fetchall()
            elif self.db_type == 'sqlite':
                query = "SELECT * FROM empleado;"
                cursor.execute(query)
                results = cursor.fetchall()

            employees = [Employee(*result) for result in results]  # Mapeo de resultados a Employee
            cursor.close()
            connection.close()
            return employees
        return []
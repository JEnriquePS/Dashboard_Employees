from sqlalchemy import Column, Integer, String, DECIMAL
from app.infrastructure.db.sqlalchemy_connector import db


class Employee(db.Model):
    __tablename__ = 'empleados'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    ciudad = Column(String(100))
    salario = Column(DECIMAL(10, 2))

    def __repr__(self):
        return f"<Empleado(nombre={self.nombre}, edad={self.edad})>"
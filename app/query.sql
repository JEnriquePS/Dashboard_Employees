CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Índice automático en id
    nombre TEXT NOT NULL,
    edad INTEGER CHECK (edad >= 0 AND edad <= 999),  -- Limitar edad a 3 dígitos
    ciudad TEXT,
    salario DECIMAL(10, 2)  -- Definir salario como decimal con 2 decimales
);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Juan Pérez', 22, 'Lima', 1500.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Ana García', 25, 'Arequipa', 1800.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Carlos Fernández', 27, 'Cusco', 2000.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Laura Gómez', 23, 'Trujillo', 1600.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Miguel López', 21, 'Chiclayo', 1400.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Lucía Martínez', 26, 'Iquitos', 1900.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Pedro Sánchez', 29, 'Piura', 2100.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Sofía Díaz', 20, 'Tacna', 1350.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('David Hernández', 28, 'Huancayo', 2050.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('María Jiménez', 30, 'Puno', 2200.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Luis Torres', 31, 'Lima', 2400.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Patricia Vega', 32, 'Arequipa', 2600.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Fernando Castro', 33, 'Cusco', 2800.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Gloria Rojas', 24, 'Trujillo', 1700.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Manuel Ruiz', 34, 'Chiclayo', 2900.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Carmen Flores', 35, 'Iquitos', 3000.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Rafael Paredes', 36, 'Piura', 3200.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Adriana Villegas', 22, 'Tacna', 1500.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Felipe Gutiérrez', 27, 'Huancayo', 2000.00);

INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES ('Teresa Navarro', 40, 'Puno', 4000.00);
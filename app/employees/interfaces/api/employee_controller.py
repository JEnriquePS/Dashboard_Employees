# app/employees/interfaces/api/employee_controller.py
from _plotly_utils.utils import PlotlyJSONEncoder
from flask import Blueprint, request, jsonify, render_template
from app.employees.services.employee_service import EmployeeService
import plotly.express as px
import pandas as pd
import json
employee_blueprint = Blueprint('employee_blueprint', __name__)
employee_service = EmployeeService()


# Ruta para crear empleados
@employee_blueprint.route('/', methods=['POST'])
def add_employee():
    data = request.json
    nombre = data.get('nombre')
    edad = data.get('edad')
    ciudad = data.get('ciudad')
    salario = data.get('salario')

    employee = employee_service.add_employee(nombre, edad, ciudad, salario)
    return jsonify({
        'id': employee.id,
        'nombre': employee.nombre,
        'edad': employee.edad,
        'ciudad': employee.ciudad,
        'salario': float(employee.salario)
    }), 201


# Ruta para listar empleados
@employee_blueprint.route('/', methods=['GET'])
def get_employees():
    employees = employee_service.list_employees()
    employees_list = [{
        'id': emp.id,
        'nombre': emp.nombre,
        'edad': emp.edad,
        'ciudad': emp.ciudad,
        'salario': float(emp.salario)
    } for emp in employees]

    return jsonify(employees_list)


@employee_blueprint.route('/dashboard/', methods=['GET'])
def show_dashboard():
    empleados = employee_service.list_employees()

    # Extraer datos de edad y salario
    data = {
        'nombre': [emp.nombre for emp in empleados],
        'edad': [emp.edad for emp in empleados],
        'salario': [float(emp.salario) for emp in empleados],
        'ciudad': [emp.ciudad for emp in empleados]
    }

    # Crear un DataFrame
    df = pd.DataFrame(data)

    # Crear el gráfico de barras
    bar_fig = px.bar(df, x='edad', y='salario', color='nombre',
                 title="Relación entre Edad y Salario",
                 labels={'edad': 'Edad', 'salario': 'Salario'},
                 height=400)
    # Crear el gráfico de pie
    pie_fig = px.pie(df, names='ciudad', title="Distribución de Personas por Ciudad", hole=0.3)

    # Convertir el gráfico a JSON
    bar_graph_json = json.dumps(bar_fig, cls=PlotlyJSONEncoder)
    pie_graph_json = json.dumps(pie_fig, cls=PlotlyJSONEncoder)

    # Renderizar el template y pasar los datos del gráfico
    return render_template('dashboard.html',
                           barGraphJSON=bar_graph_json,
                           pieGraphJSON=pie_graph_json,
                           empleados=empleados)
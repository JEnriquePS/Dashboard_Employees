# main.py
from flask import Flask
from config import Config
from app.infrastructure.db.sqlalchemy_connector import init_db
from app.employees.interfaces.api.employee_controller import employee_blueprint


def create_app():
    app = Flask(__name__)
    # Cargar la configuración
    app.config.from_object(Config)
    # Inicializar la base de datos
    init_db(app)
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)

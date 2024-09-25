
class Config:
    # Sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///employees.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/employees.db'
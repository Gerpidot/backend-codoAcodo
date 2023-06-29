from flask_sqlalchemy import SQLAlchemy


# Crea una instancia de SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    



class Users(db.Model):  # Users hereda de db.Model
    """
    Definición de la tabla users en la base de datos.
    La clase Users hereda de db.Model.
    Esta clase representa la tabla "users" en la base de datos.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100))
    token = db.Column(db.String(400))

    def __init__(self, name, lastname, password, email,token):
        """
        Constructor de la clase Producto.

        Args:
            name (str): Nombre del usuario.
            lastname (str): apellido del usuario.
            password (str): clave del usuario.
            email (str): correo del user.
            token (str): posible clave para usar mas adelante
        """
        self.name = name
        self.lastname = lastname
        self.password = password
        self.email = email
        self.token=token

    # Se pueden agregar más clases para definir otras tablas en la base de datos
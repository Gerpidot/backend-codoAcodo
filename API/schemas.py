# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow

ma = Marshmallow()
def init_ma(app):
    ma.init_app(app)



# Definición del esquema para la clase Users
class UsersSchema(ma.Schema):
    """
    Esquema de la clase Users.

    Este esquema define los campos que serán serializados/deserializados
    para la clase User.
    """
    class Meta:
        fields = ("id", "name", "lastname", "email", "password","token")

user_schema = UsersSchema()  # Objeto para serializar/deserializar un producto
users_schema = UsersSchema(many=True)  # Objeto para serializar/deserializar múltiples productos

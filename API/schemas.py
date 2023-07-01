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
        fields = ("id", "name", "lastname", "email", "password", "token")


user_schema = UsersSchema()  # Objeto para serializar/deserializar un producto
# Objeto para serializar/deserializar múltiples productos
users_schema = UsersSchema(many=True)


class PostSchema(ma.Schema):
    """
    Esquema de la clase Post.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Post.
    """
    class Meta:
        fields = ("id", "title", "content", "user_id")


post_schema = PostSchema()  # Objeto para serializar/deserializar un producto
posts_schema = PostSchema(many=True)

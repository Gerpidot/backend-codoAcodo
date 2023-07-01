
# En este archivo se declaran las funciones para las rutas de la api
from API.models import Users, Post, db
from API.schemas import user_schema, users_schema, post_schema
from flask import jsonify, request
from utils.utils import validar_email


# route "/" mensaje saludo quedó acá pero iría en otro lado, en app.py :D


def hello():
    return "Servidor de prueba para codoacodo"

# Controladores para la clase User
# get all users


def get_Users():

    all_users = Users.query.all()  # Obtiene todos los registros de la tabla de productos
    # Serializa los registros en formato JSON
    result = users_schema.dump(all_users)
    # Retorna el JSON de todos los registros de la tabla
    return users_schema.jsonify(result)


def post_User():
  # Faltan validaciones miles
    try:
        email = request.json["email"]
        # Validaciones
        # Que el email sea correcto
        if validar_email(email) == False:
            message = "El email no es correcto"
            response = {"message": message}
            return response

        # Que no exista un usuario con el mismo email
        # Busca en la tabla el email indicado
        usuario = Users.query.filter_by(email=email).first()
        if usuario:  # Si es true es porque encontró un registro
            message = "Ya existe un usuario registrado con ese email"
            response = {"message": message}
            return response
        print(usuario)
        # Obtiene el nombre del usuario del JSON proporcionado
        name = request.json["name"]
        # Obtiene el apellido del usuario del JSON proporcionado
        lastname = request.json["lastname"]
        # Obtiene el email del usuario del JSON proporcionado
        email = request.json["email"]
        # Obtiene el password del usuario del JSON proporcionado
        password = request.json["password"]
        token = request.json["token"]  # idem token

        # Crea un nuevo objeto Users con los datos proporcionados
        new_user = Users(name, lastname, password, email, token)

        # Agrega el nuevo user a la sesión de la base de datos
        db.session.add(new_user)
        db.session.commit()  # Guarda los cambios en la base de datos

        # Retorna el JSON del nuevo usuario creado
        return user_schema.jsonify(new_user)
    except Exception as ex:
        print(ex)
        return "Algo no salió como se esperaba (básico)"


def put_User(id):
    try:

        """
        Endpoint para actualizar un usuario existente en la base de datos.

        Lee los datos proporcionados en formato JSON por el cliente y actualiza el registro del usuario con el ID especificado.
        Retorna un JSON con el producto actualizado.
        """

        # Obtiene el usuario existente con el ID especificado
        usuario = Users.query.get(id)
        # Validaciones
        # Que exista el usuario a editar
        if usuario is None:
            message = "No existe un usuario con ese id"
            response = {"message": message}
            return response
        # Actualiza los atributos del usuario con los datos proporcionados en el JSON

        usuario.name = request.json["name"]
        usuario.lastname = request.json["lastname"]
        usuario.email = request.json["email"]
        usuario.password = request.json["password"]
        usuario.token = request.json["token"]

        db.session.commit()  # Guarda los cambios en la base de datos
        # Retorna el JSON del producto actualizado
        return user_schema.jsonify(usuario)

    except Exception as ex:
        print(ex)
        return "Algo falló al intentar actualizar el usuario"


def update_Password():
    try:
        email = request.json["email"]
        # Validaciones
        # Que el email sea correcto
        if validar_email(email) == False:
            message = "El email no es correcto"
            response = {"message": message}
            return response

        # Que SI exista un usuario con ese  email
        # Busca en la tabla el email indicado
        usuario = Users.query.filter_by(email=email).first()

        if usuario is None:  # Si es false es porque No encontró un registro
            message = "No existe un usuario registrado con ese email"
            response = {"message": message}
            return response
        # Se encontró el usuario se envía un email al usuario
        # Para confirmar el cambio, posteriormente se guarda el nuevo password :D

        # La f delante de un string es como en js las `${}`
        response = {
            "message": 'Te enviamos un email para que puedas recuperar tu contraseña.'}
        return response
    except Exception as ex:
        print(ex)
        return "Algo falló al intentar actualizar la contraseña"


def delete_User():
    try:
        userId = request.json["user_id"]  # Obtiene el id del user
        toDeleteUser = Users.query.get(userId)  # Se busca el user
        if toDeleteUser is None:
            message = "No existe un usuario con ese id"
            response = {"message": message}
            return response

        db.session.delete(toDeleteUser)  # se indica borrar el usuario
        db.session.commit()  # Se realizan las acciones en la base
        response = {'message': "Se eliminó el usuario correctaente"}
        return response

    except Exception as ex:
        print(ex)
        response = {'message': "Hubo un error al intentar eliminar el usuario"}
        return response

# Post methods


def post_Post():
  # Faltan validaciones miles
    try:
        title = request.json["title"]
        content = request.json["content"]
        userId = request.json["user_id"]
        # Validaciones
        # Que exista el usuario
        user = Users.query.get(userId)
        print("UUUSERRR", user)
        if user is None:
            response = {"message": "No existe un usuario con ese id"}
            return response
        # titulo y contente son obligatorios
        if (title or content) == "":
            message = "El título y el mensaje deben completarse"
            response = {"message": message}
            return response

        # Crea un nuevo objeto Post con los datos proporcionados
        new_post = Post(title, content, userId)

        # Agrega el nuevo user a la sesión de la base de datos
        db.session.add(new_post)
        db.session.commit()  # Guarda los cambios en la base de datos

        # Retorna el JSON del nuevo usuario creado
        return post_schema.jsonify(new_post)
    except Exception as ex:
        print(ex)
        return "No se pudo crear el post"

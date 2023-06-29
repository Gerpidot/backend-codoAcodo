#En este archivo se declaran las funciones para las rutas de la api

from API.models import Users,db
from API.schemas import user_schema,users_schema
from flask import  jsonify, request
from utils.utils import validar_email

#route "/" mensaje saludo
def hello():
    return "Servidor de prueba para codoacodo"

#Controladores para la clase User
#get all users

def get_Users():
    """
    Endpoint para obtener todos los users de la base de datos.

    Retorna un JSON con todos los registros de la tabla de productos.
    """
    all_users = Users.query.all()  # Obtiene todos los registros de la tabla de productos
    result = users_schema.dump(all_users)  # Serializa los registros en formato JSON
    return users_schema.jsonify(result)  # Retorna el JSON de todos los registros de la tabla

def post_User():
  #Faltan validaciones miles
 try:
    email = request.json["email"]
    #Validaciones
    #Que el email sea correcto 
    if validar_email(email)==False:
        message="El email no es correcto"
        response={"message":message}
        return response

    #Que no exista un usuario con el mismo email
    usuario=Users.query.filter_by(email=email).first()#Busca en la tabla el email indicado
    if usuario: #Si es true es porque encontró un registro
        message="Ya existe un usuario registrado con ese email"
        response={"message":message}
        return response

    name = request.json["name"]  # Obtiene el nombre del usuario del JSON proporcionado
    lastname = request.json["lastname"]  # Obtiene el apellido del usuario del JSON proporcionado
    email = request.json["email"]  # Obtiene el email del usuario del JSON proporcionado
    password = request.json["password"]  # Obtiene el password del usuario del JSON proporcionado
    token=request.json["token"] #idem token
    
    new_user = Users(name, lastname, email, password,token)  # Crea un nuevo objeto Users con los datos proporcionados
    
    db.session.add(new_user)  # Agrega el nuevo user a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    
    return user_schema.jsonify(new_user)  # Retorna el JSON del nuevo usuario creado
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
        
        usuario = Users.query.get(id)  # Obtiene el usuario existente con el ID especificado
        #Validaciones
        #Que exista el usuario a editar
        if usuario is None:
            message="No existe un usuario con ese id"
            response={"message":message}
            return response
        # Actualiza los atributos del usuario con los datos proporcionados en el JSON
        
        usuario.name = request.json["name"]
        usuario.lastname = request.json["lastname"]
        usuario.email = request.json["email"]
        usuario.password = request.json["password"]
        usuario.token=request.json["token"]

        db.session.commit()  # Guarda los cambios en la base de datos
        return user_schema.jsonify(usuario)  # Retorna el JSON del producto actualizado

    except Exception as ex:
        print(ex)
        return "Algo falló al intentar actualizar el usuario"
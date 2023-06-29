from flask import Blueprint
from API.controllers import hello,get_Users,post_User,put_User

# Crea un Blueprint para las rutas
bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
 return hello()


@bp.route('/users', methods=["GET"])
def getAllUsers():
    return get_Users()

@bp.route('/users', methods=["POST"])
def postUser():
    return post_User()

@bp.route('/users/<id>',methods=["PUT"])
def putUser(id):
    # Llama a la función importada desde el controlador
    return put_User(id)
    
   
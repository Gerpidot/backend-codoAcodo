from flask import Blueprint, render_template
# from API.controllers import hello,get_Users,post_User,put_User,update_Password
import API.controllers as control

# Crea un Blueprint para las rutas
bp = Blueprint('routes', __name__)


@bp.route('/')
def home():
    return render_template("index.html")


@bp.route('/users', methods=["GET"])
def getAllUsers():
    return control.get_Users()


@bp.route('/users', methods=["POST"])
def postUser():
    return control.post_User()

@bp.route('/users/login',methods=["POST"])
def loginUser():
    return control.login_User()

@bp.route('/users/<id>', methods=["PUT"])
def putUser(id):
    # Llama a la función importada desde el controlador
    return control.put_User(id)


@bp.route('/users/forgot', methods=["POST"])
def updatePassword():
    return control.update_Password()


@bp.route('/users', methods=["DELETE"])
def deleteUsers():
    return control.delete_User()

# POOOST routes


@bp.route('/posts', methods=['POST'])
def postPost():
    return control.post_Post()


@bp.route('/posts', methods=['DELETE'])
def deletePost():
    return control.delete_Post()


@bp.route('/posts/<id>', methods=['PUT'])
def putPost(id):
    return control.put_Post(id)


@bp.route('/posts', methods=['GET'])
def getPost():
    return control.get_Post()

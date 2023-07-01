# Importa las clases Flask, jsonify y request del módulo flask
from flask import Flask, jsonify, request, redirect, url_for
# Importa la clase CORS del módulo flask_cors
from flask_cors import CORS
# Importa la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow

# Se importan las rutas
from API.routes import bp as routes_bp
# Se crea la instancia de alquemy con la app con init_db y se trae db para usar con el context
from API.models import init_db, db
# Se inicia y crea la inatancia de marshmalow
from API.schemas import init_ma, ma
# from swagger_gui.swagger_gui import init_api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Resource, Api
import json
'''
En este código, se está creando una instancia de la clase Flask y se está configurando para permitir el acceso cruzado entre dominios utilizando el módulo CORS.

app = Flask(__name__): Se crea una instancia de la clase Flask y se asigna a la variable app. El parámetro __name__ es una variable que representa el nombre del módulo o paquete en el que se encuentra este código. Flask utiliza este parámetro para determinar la ubicación de los recursos de la aplicación.

CORS(app): Se utiliza el módulo CORS para habilitar el acceso cruzado entre dominios en la aplicación Flask. Esto significa que el backend permitirá solicitudes provenientes de dominios diferentes al dominio en el que se encuentra alojado el backend. Esto es útil cuando se desarrollan aplicaciones web con frontend y backend separados, ya que permite que el frontend acceda a los recursos del backend sin restricciones de seguridad del navegador. Al pasar app como argumento a CORS(), se configura CORS para aplicar las políticas de acceso cruzado a la aplicación Flask representada por app.

'''
# Crea una instancia de la clase Flask con el nombre de la aplicación
app = Flask(__name__)
# Configura CORS para permitir el acceso desde el frontend al backend
CORS(app)

'''
En este código, se están configurando la base de datos y se están creando objetos para interactuar con ella utilizando SQLAlchemy y Marshmallow.

app.config["SQLALCHEMY_DATABASE_URI"]: Se configura la URI (Uniform Resource Identifier) de la base de datos. En este caso, se está utilizando MySQL como el motor de base de datos, el usuario y la contraseña son "root", y la base de datos se llama "proyecto". Esta configuración permite establecer la conexión con la base de datos.

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]: Se configura el seguimiento de modificaciones de SQLAlchemy. Al establecerlo en False, se desactiva el seguimiento automático de modificaciones en los objetos SQLAlchemy, lo cual mejora el rendimiento.

db = SQLAlchemy(app): Se crea un objeto db de la clase SQLAlchemy, que se utilizará para interactuar con la base de datos. Este objeto proporciona métodos y funcionalidades para realizar consultas y operaciones en la base de datos.

ma = Marshmallow(app): Se crea un objeto ma de la clase Marshmallow, que se utilizará para serializar y deserializar objetos Python a JSON y viceversa. Marshmallow proporciona una forma sencilla de definir esquemas de datos y validar la entrada y salida de datos en la aplicación. Este objeto se utilizará para definir los esquemas de los modelos de datos en la aplicación.

'''
# Configura la URI de la base de datos con el driver de MySQL, usuario, contraseña y nombre de la base de datos
# URI de la BD == Driver de la BD://user:password@UrlBD/nombreBD
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/proyecto"
# Datos de conecxion a la db
# Conecction para pythonanywhere
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://Gerpidot:ezpaesjuge@Gerpidot.mysql.pythonanywhere-services.com/Gerpidot$default"
# Conecction para localhost
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://paydot:ezpaesjuge@localhost/codoacodo"
# Configura el seguimiento de modificaciones de SQLAlchemy a False para mejorar el rendimiento
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# La instancia de la clase SQLAlchemy secrea en models
# Inicializa la instancia de SQLAlchemy
init_db(app)
# La instancia de la clase Marshmallow se crea en schemas
# Inicia la instancia de Marshmallow con la app
init_ma(app)
# Registra el Blueprint de las rutas
app.register_blueprint(routes_bp)

# Crea  la instancia de API con la app, para swagger

api = Api(app)

# Configure Swagger UI
SWAGGER_URL = '/docs'
API_URL = '/openapi.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "CAC Test EndPoints"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)





@app.route('/openapi.json')
def swagger():
    with open('openapi.json', 'r') as f:
        return jsonify(json.load(f))


with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos

# Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)

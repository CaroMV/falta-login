#Se encarga de crear la aplicacion e inicializarla
from flask import Flask

app = Flask(__name__)

#tambien la clave secreta para la sesión se guarda acá

app.secret_key="cualquier clave"
from flask_app import app #Importamos la app de la carpeta flask_app
#
#--------- IMPORTAR LOS CONTROLADORES QUE USE
from flask_app.controllers import usuarios
# from flask_app.controllers import peliculas


if __name__=="__main__": #Ejecutamos la aplicación

   app.run(debug=True)

#python -m pipenv install flask pymysql flask-bcrypt
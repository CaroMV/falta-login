#Dentro de controladores se encuentran las rutas de esas entidades 
#Rutas de transito del objeto Usuario
#!ESTAS DOS LINEAS DE CODIGO SE REPITEN
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_bcrypt import Bcrypt

#importar las clases que necesito 

from flask_app.models.usuario import Usuario

#PARA ENCRIPTAR LAS CONTRASEÑAS DEBO CREAR UN OBJETO LLAMADO BCRYPT

bcrypt= Bcrypt(app)

#ruta inico
@app.route('/')
def inicio():
    return render_template('index.html')

#ruta para procesar registro
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    #1 validar la informacion
    if not Usuario.validar_registro(request.form):
        return redirect('/')
    #2. encriptar contraseña
    password_hash= bcrypt.generate_password_hash(request.form['password'])

    datos={
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': password_hash,
    }

    #guardar nuevo dato e iniciar sesión
    id_nuevo= Usuario.save(datos)
    session['usuario_id']= id_nuevo
    session['nombre']= request.form['nombre']

    return redirect('/hola')

#ruta para procesar login

#lugar donde entramos cuando logeamos
@app.route('/hola')
def hola():
    if 'usuario_id' not in session:
        return redirect('/')

    
    return render_template('hola.html')

#cerrar sesión

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return redirect('/')
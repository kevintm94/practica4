from app import app, db
from flask import render_template, redirect
import formularios
from models import Tarea

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', subtitulo="Actividad en grupo TAI")

@app.route('/sobrenosotros', methods=['GET', 'POST'])
def sobrenosotros():
 
    form_agregar = formularios.FormAgregarTareas()
    form_eliminar = formularios.FormEliminarTarea()

    if form_agregar.validate_on_submit():
        nueva_tarea = Tarea(titulo=form_agregar.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()

    if form_eliminar.validate_on_submit() and form_eliminar.id_tarea.data:
        tarea = Tarea.query.get(form_eliminar.id_tarea.data)
        if tarea:
            db.session.delete(tarea)
            db.session.commit()
        return redirect('/sobrenosotros')

    return render_template('sobrenosotros.html', 
                           form_agregar=form_agregar, 
                           form_eliminar=form_eliminar)

@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'
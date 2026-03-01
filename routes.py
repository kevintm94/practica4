from app import app, db
from flask import render_template, redirect, url_for, request
import formularios
from models import Tarea


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', subtitulo = "Actidad en grupo TAI")

@app.route('/sobrenosotros', methods = ['GET', 'POST'])
def sobrenosotros():
    formulario = formularios.FormAgregarTareas()
    tareas = Tarea.query.all()
    
    if formulario.validate_on_submit() :
        nueva_tarea = Tarea(titulo = formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()
        print('Se envio correctamente', formulario.titulo.data)
        return redirect(url_for('sobrenosotros'))
    
    return render_template('sobrenosotros.html', form = formulario, tareas = tareas)

@app.route('/editar_tarea/<int:id>', methods=['GET', 'POST'])
def editar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    formulario = formularios.FormEditarTareas()
    
    if formulario.validate_on_submit():
        tarea.titulo = formulario.titulo.data
        db.session.commit()
        print('Tarea actualizada correctamente')
        return redirect(url_for('sobrenosotros'))
    elif request.method == 'GET':
        formulario.titulo.data = tarea.titulo
    
    return render_template('editar_tarea.html', form = formulario, tarea = tarea)

@app.route('/eliminar_tarea/<int:id>')
def eliminar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    print('Tarea eliminada correctamente')
    return redirect(url_for('sobrenosotros'))
    
@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola{nombre} bienvenido a Taller Apps '
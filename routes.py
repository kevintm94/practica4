from app import app, db
from flask import render_template, redirect, url_for, request
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
    tareas = Tarea.query.all()

    # agregar nueva tarea
    if form_agregar.validate_on_submit() and form_agregar.enviar.data:
        nueva_tarea = Tarea(titulo=form_agregar.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()
        print('Se envio correctamente', form_agregar.titulo.data)
        return redirect(url_for('sobrenosotros'))

    # eliminar por id
    if form_eliminar.validate_on_submit() and form_eliminar.eliminar.data:
        tarea = Tarea.query.get(form_eliminar.id_tarea.data)
        if tarea:
            db.session.delete(tarea)
            db.session.commit()
            print('Tarea eliminada correctamente (desde formulario)')
        return redirect(url_for('sobrenosotros'))

    return render_template(
        'sobrenosotros.html',
        form_agregar=form_agregar,
        form_eliminar=form_eliminar,
        tareas=tareas,
    )
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
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'
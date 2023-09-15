from flask import Blueprint, redirect, render_template, flash, url_for, request, jsonify 
from models.cinexs import *
from utils.utils import *
from utils.utils import encriptar_contrasena




galeria = Galeria()


cinex= Blueprint('cinex', __name__)

@cinex.route('/')
def Index():
    result= galeria.consultar_galeria()
    return render_template('index.html', galerias = result)

@cinex.route('/ingreso')
def Ingreso():
    result= galeria.consultar_galeria()
    return render_template('galeria.html', galerias = result)

@cinex.route('/add_ingreso', methods = ['POST'])
def add_ingreso():
    try:
        if request.method == 'POST':
            galeria.setTitulo(request.form['titulo'])
            galeria.setFotografo(request.form['fotografo'])
            galeria.setNota(request.form['nota'])
            galeria.setLugar(request.form['lugar'])
            galeria.setCiudad(request.form['ciudad'])
            galeria.setProvincia(request.form['provincia'])
            galeria.setFecha(request.form['fecha'])
            imagen = guardar_archivo_upload(request.files['imagen'])
            galeria.setImagen(imagen)
            galeria.insertar_galeria()
            return redirect(url_for('cinex.Ingreso'))
    except Exception as e:
        raise e

@cinex.route('/galeria/json/<string:id>')
def jsonIngreso(id):
    galeria.setIdgaleria(id)
    result = galeria.consultar_galeria_id()
    print(result)
    result = jsonify(result)
    return result

@cinex.route('/galeria/update/<id>', methods = ['POST'])
def update_ingreso(id):
    try:
        if request.method == 'POST':
            galeria.setIdgaleria(id)
            galeria.setFotografo(request.form['idgaleria'])
            galeria.setTitulo(request.form['titulo'])
            galeria.setNota(request.form['nota'])
            galeria.setLugar(request.form['lugar'])
            galeria.setCiudad(request.form['ciudad'])
            galeria.setProvincia(request.form['provincia'])
            galeria.setFecha(request.form['fecha'])
            imagen = guardar_archivo_upload(request.files['imagen'])
            galeria.setImg(imagen)
            galeria.editar_galeria
            print(galeria.getIdgaleria())
            return redirect(url_for('cinex.Ingreso'))
    except Exception as e:
        raise e

@cinex.route('/delete_galeria/<string:idgaleria>')
def delete_galeria(idgaleria):
    galeria.setIdgaleria(idgaleria)
    galeria.eliminar_galeria()
    return redirect(url_for('cinex.Ingreso'))


    

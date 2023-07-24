from flask import Blueprint, redirect, render_template, flash, url_for, request
from models.cinexs import *
import os

cliente=Clientes()
pelicula = Peliculas()
cinex= Blueprint('cinex', __name__)

#Cliente

@cinex.route('/cliente')
def Cliente():
    result = cliente.consultar_cliente()
    return render_template('clientes.html', clientes = result)

@cinex.route('/add_cliente', methods = ['POST'])
def add_cliente():
    try:
        if request.method == 'POST':
            cliente.setCliente_id(request.form['cliente_id'])
            cliente.setNombre(request.form['nombre'])
            cliente.setApellido(request.form['apellido'])
            cliente.setEmail(request.form['email'])
            cliente.setTelefono(request.form['telefono'])
            cliente.insertar_cliente()
            return redirect(url_for('cinex.Cliente'))
    except Exception as e:
        raise e

@cinex.route('/delete_cliente/<string:cliente_id>')
def delete_cliente(cliente_id):
    cliente.setCliente_id(cliente_id)
    cliente.eliminar_cliente()
    return redirect(url_for('cinex.Cliente'))

#Peliculas
@cinex.route('/pelicula')
def Pelicula():
    result = pelicula.consultar_pelicula()
    return render_template('peliculas.html', peliculas = result)

@cinex.route('/add_pelicula', methods = ['POST'])
def add_pelicula():
    try:
        if request.method == 'POST':
            pelicula.setTitulo(request.form['titulo'])
            pelicula.setGenero(request.form['genero'])
            pelicula.setDuracion(request.form['duracion'])
            pelicula.setClasificacion(request.form['clasificacion'])
            pelicula.setImg(request.form['img'])
            pelicula.setSipnosis(request.form['sipnosis'])

            pelicula.insertar_pelicula()
            return redirect(url_for('cinex.Pelicula'))
    except Exception as e:
        raise e
def subir_archivo():
    if request.method == "POST":
        archivo = request["img"]
        if archivo:
            # Ruta donde se guardará el archivo en el servidor
            ruta_guardado = os.path.join("images", archivo.filename)
            archivo.save(ruta_guardado)
            return f"El archivo {archivo.filename} se ha subido correctamente."
    return redirect(url_for('cinex.Pelicula'))






"""
@flaskcontac.route('/edit/<string:id>', methods= ['GET', 'POST'])
def get_contac(id):
    try:
        contac.setSQL(mysql)
        contac.setId(id)
        data= contac.modifcontacId()
        return render_template('edit_contac.html', contac = data)
    except Exception as e:
        print(e)

@flaskcontac.route('/update/<id>', methods = ['POST'])
def update_contac(id):
    if request.method == 'POST':
        contac.setFullname(request.form['fullname'])
        contac.setPhone(request.form['phone'])
        contac.setEmail(request.form['email'])
        contac.setId(id)
        contac.modifcontac()
        return redirect(url_for('flaskcontac.Index')) 

@flaskcontac.route('/delete/<string:id>')
def delete_contac(id):
    contac.setSQL(mysql)
    contac.setId(id)
    data = contac.ellimcontac()
    flash('Contacto removido')
    return redirect(url_for('flaskcontac.Index'))
"""


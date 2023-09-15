from flask import flash
from utils.accesobd import *
from typing import Any

class Galeria():
    def setIdgaleria(self, idgaleria):
        self.__idgaleria = idgaleria
    def getIdgaleria(self):
        return self.__idgaleria

    def setTitulo(self, titulo):
        self.__titulo = titulo
    def getTitulo(self):
        return self.__titulo

    def setFotografo(self, fotografo):
        self.__fotografo = fotografo
    def getFotografo(self):
        return self.__fotografo

    def setNota(self, nota):
        self.__nota = nota
    def getNota(self):
        return self.__nota

    def setLugar(self, lugar):
        self.__lugar = lugar
    def getLugar(self):
        return self.__lugar

    def setCiudad(self, ciudad):
        self.__ciudad = ciudad
    def getCiudad(self):
        return self.__ciudad

    def setProvincia(self, provincia):
        self.__provincia = provincia
    def getProvincia(self):
        return self.__provincia

    def setFecha(self, fecha):
        self.__fecha = fecha
    def getFecha(self):
        return self.__fecha

    def setImagen(self, imagen):
        self.__imagen = imagen
    def getImagen(self):
        return self.__imagen

    def consultar_galeria(self):
        insert = consultarbd('SELECT idgaleria, titulo, fotografo, nota, lugar, ciudad, provincia, fecha, imagen FROM galeria;')
        return insert
    def consultar_galeria_id(self):
        sql = 'SELECT idgaleria, titulo, fotografo, nota, lugar, ciudad, provincia, fecha, imagen FROM galeria where idgaleria = {0}'.format(self.getIdgaleria())
        data = consultarbd(sql)
        return data[0]

    def insertar_galeria(self):
        sql= 'INSERT INTO galeria (titulo, fotografo, nota, lugar, ciudad, provincia, fecha,imagen) VALUES (%s, %s, %s,%s,%s, %s,%s,%s)'
        data = ( self.getTitulo(), self.getFotografo(), self.getNota(), self.getLugar(), self.getCiudad(), self.getProvincia(),self.getFecha(), self.getImagen())
        actualizarbd(sql,data)
        flash("Cliente Ingresado!")

    def eliminar_galeria(self):
        sql='DELETE FROM galeria WHERE idgaleria= {0}'.format(self.getIdgaleria())
        actualizarbd(sql)
        flash('Cliente Removido!')

    def editar_galeria(self):
        sql='UPDATE galeria SET idgaleria = %s, titulo = %s, fotografo=%s, nota= %s, lugar=%s , ciudad =%s, provincia =%s, fecha =%s, imagen =%s  WHERE idgaleria ={0}'.format(self.getIdgaleria())
        data = (self.getIdgaleria(), self.getTitulo(), self.getFotografo(), self.getNota(), self.getLugar(), self.getCiudad(), self.getProvincia(),self.getFecha(), self.getImagen())
        actualizarbd(sql,data)
        flash("Cliente Actualizado")




    
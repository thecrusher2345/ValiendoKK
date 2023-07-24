from flask import flash
from utils.accesobd import *

class Clientes():
    #Cedula de los clientes
    
    #Metodos
    def setCliente_id(self, cliente_id):
        self.__cliente_id= cliente_id
    def getCliente_id(self):
        return self.__cliente_id
    
    def setNombre(self, nombre):
        self.__nombre= nombre
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido= apellido
    def getApellido(self):
        return self.__apellido
    
    def setEmail(self, email):
        self.__email= email
    def getEmail(self):
        return self.__email
    
    def setTelefono(self,telefono):
        self.__telefono= telefono
    def getTelefono(self):
        return self.__telefono
    
    def setSQL(self, mysql):
        self.__mysql= mysql
    def getSQL(self):
        return self.__mysql

    def consultar_cliente(self):
        insert = consultarbd('SELECT * FROM clientes c;')
        return insert

    def insertar_cliente(self):
        sql= 'INSERT INTO clientes (cliente_id, nombre, apellido, email, telefono) VALUES (%s, %s, %s,%s,%s)'
        data = (self.getCliente_id(),self.getNombre(),self.getApellido(),self.getEmail(),self.getTelefono())
        actualizarbd(sql,data)
        flash("Contacto Ingresado Correctamente!")

    def eliminar_cliente(self):
        sql='DELETE FROM clientes WHERE cliente_id= {0}'.format(self.getCliente_id())
        actualizarbd(sql)
        flash('Contacto Removido con Exito!')

#Pelciulas
class Peliculas():

    def setPelicula_id(self, pelicula_id):
        self.__pelicula_id= pelicula_id
    def getPelciula_id(self):
        return self.__pelicula_id

    def setTitulo(self, titulo):
        self.__titulo= titulo
    def getTitulo(self):
        return self.__titulo
    
    def setGenero(self, genero):
        self.__genero= genero
    def getGenero(self):
        return self.__genero
    
    def setDuracion(self, duracion):
        self.__duracion= duracion
    def getDuracion(self):
        return self.__duracion
    
    def setClasificacion(self, clasificacion):
        self.__clasificacion = clasificacion
    def getClasificacion(self):
        return self.__clasificacion
    
    def setImg(self, img):
        self.__img=img
    def getImg(self):
        return self.__img
    
    def setSipnosis(self,sipnosis):
        self.__sipnosis= sipnosis
    def getSipnosis(self):
        return self.__sipnosis
    
    def consultar_pelicula(self):
        insert = consultarbd('SELECT * FROM peliculas p;')
        return insert
    
    def insertar_pelicula(self):
        sql= 'CALL InsertarNuevaPelicula(%s, %s, %s, %s, %s, %s);'
        data = (self.getTitulo(),self.getGenero(),self.getDuracion(),self.getClasificacion(),self.getImg(), self.getSipnosis())
        actualizarbd(sql,data)
        flash("Contacto Actualizado Correctamente!")

    
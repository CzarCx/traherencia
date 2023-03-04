# -*- coding: utf-8 -*-

class Alumno:
    
    def __init__(self,nombre,boleta,grupo):
        self.nombre = nombre
        self.boleta = boleta
        self.grupo = grupo
        
  """  def guardar():
        archivo=open(archivo.csv, a)
        archivo.write("Nombre:", self.nombre)
        archivo.write("Boleta:", self.boleta)
        archivo.write("Grupo:", self.grupo)
        archivo.close"""
        
    def getNombre(self):
        return self.nombre
    
    def getBoleta(self):
        return self.boleta
    
    def getGrupo(self):
        return self.grupo
    
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setBoleta(self,boleta):
        self.__boleta = boleta
        
    def setgrupo(self,grupo):
        self.__grupo = grupo


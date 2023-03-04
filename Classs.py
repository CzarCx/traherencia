# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:53:10 2023

@author: César
"""
from tkinter import *
nombre=str()
class DatosA:
    def __init__(self,nombre,apellidop,apellidoma,boleta,grupo):
        self.nombre=nombre
        self.apellidop=apellidop
        self.apellidoma=apellidoma
        self.boleta=boleta
        self.grupo=grupo
            
    def getNombre(self):
        return self.__nombre
    
    def getApellidopa (self):
        return self.__apellidop
    
    def getApellidoma (self):
        return self.__apellidoma
    
    def getBoleta (self):
        return self.__boleta
    
    def getGrupo (self):
        return self.__grupo
    
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def setApellidopa (self,apellidop):
        self.__apellidop=apellidop
    
    def setApellidoma (self,apellidoma):
        self.__apellidoma=apellidoma

    def setBoleta(self,boleta):
        self.__boleta=boleta
    
    def setGrupo(self,grupo):
        self.__grupo=grupo
        
    def guardar(self): 
        
        archivo=open("archivo2.txt","a")
        archivo.write("\n")
        archivo.write("Nombre: " + self.nombre)
        archivo.write("\n")
        archivo.write("Apellido Paterno: " + self.apellidop)
        archivo.write("\n")
        archivo.write("Apellido Materno: " + self.apellidoma)
        archivo.write("\n")
        archivo.write("Boleta: " + self.boleta)
        archivo.write("\n")
        archivo.write("Grupo: " + self.grupo)
        archivo.write("\n")
        archivo.close()
    

class DatosM:
    def __init__(self,nombre,apellidop,apellidoma,boleta,grupo):
        self.nombre=nombre
        self.apellidop=apellidop
        self.apellidoma=apellidoma
        self.boleta=boleta
        self.grupo=grupo
            
    def getNombre(self):
        return self.__nombre
    
    def getApellidop (self):
        return self.__apellidop
    
    def getApellidoma (self):
        return self.__apellidoma
    
    
    def getBoleta (self):
        return self.__boleta
    
    
    def getGrupo (self):
        return self.__grupo
    
    
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def setApellidopa (self,apellidop):
        self.__apellidopa=apellidop
    
    def setApellidoma (self,apellidoma):
        self.__apellidoma=apellidoma
    
    def setBoleta(self,boleta):
        self.__boleta=boleta
    
    
    def setGrupo(self,grupo):
        self.__grupo=grupo

    def guardar(self): 
        
        archivo=open("archivo.txt","a")
        archivo.write("\n")
        archivo.write("Nombre: " + self.nombre)
        archivo.write("\n")
        archivo.write("Apellido Paterno: " + self.apellidop)
        archivo.write("\n")
        archivo.write("Apellido Materno: " + self.apellidoma)
        archivo.write("\n")
        archivo.write("Boleta: " + self.boleta)
        archivo.write("\n")
        archivo.write("Grupo: " + self.grupo)
        archivo.write("\n")
        archivo.close()
            
        
        
class DatosSesion:
    
    def __init__(self,usuario,contraseña):
        self.usuario=usuario
        self.contraseña=contraseña
        
        
    def getUsuario (self):
            return self.__usuario
        
    def setUsuario(self,usuario):
            self.__usuario=usuario
            
    
    def getContraseña (self):
        return self.__contraseña
    
    def setContraseña(self,contraseña):
        self.__contraseña=contraseña
        
def guardar():
    c=open(archivo.csv,a)
    archivo.write("Nombre: ",self.nombre)
    archivo.write("Apellido Paterno: " + self.apellidop)
    archivo.write("Apellido Materno: " + self.apellidoma)
    archivo.write("Boleta: ",self.boleta)
    archivo.write("Grupo: ",self.grupo)
    archivo.close
        
def consultar():
    archivo=open("archivo.csv",r)
    registros=archivo.read()
    messagebox.showinfo("Registros: ",registros)
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:27:31 2023

@author: César
"""
from tkinter import *
 

class ventanaSele :
    def abrirSele():
        raiz=Tk()        
        raiz.title("Esta es mi put# ventana") 
        raiz.config(bg="#FFB4A4")
                
        miFrame=Frame() 
        miFrame.pack(fill="both", expand="True")
        miFrame.config(bg="white")
        miFrame.config(width="400",height="350") 
        miFrame.config(bd=39) 
        miFrame.config(relief="groove") 
        
        
        selec=Label(miFrame, text="Seleciona el tipo de usuario que eres:", fg="black")
        selec.pack()
        selec.place(x=70, y=50)
        selec.config(bg="white", relief="flat")
        
        def butonalum():
            raiz.destroy()
            from ventana3 import ventanaAlu
            ventanaAlu.abrirAlu()
            
        def botonprof():
            raiz.destroy()
            from ventanaMa import ventaMaster
            ventaMaster.abrirMaestro()
        
        
        butonprofe=Button(miFrame, text="Profesor", command=botonprof)
        butonprofe.pack()
        butonprofe.place(x=70,y=150)
        butonprofe.config(cursor="hand2")
        butonalum=Button(miFrame, text="Alumno", command=butonalum)
        butonalum.pack()
        butonalum.place(x=200,y=150)
        butonalum.config(cursor="hand2")
            
        raiz.mainloop()
        
        

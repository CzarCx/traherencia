from tkinter import *
import tkinter as tk
from Classs import DatosM
from io import *

class ventaMaster():
    def abrirMaestro():
        raiz=Tk()  
        raiz.title("Esta") 
        raiz.iconbitmap("messi.ico")
        raiz.config(bg="#FFB4A4")
        raiz.resizable(False,False)
        raiz.geometry("700x400")
                
        miFrame=Frame() 
        miFrame.pack(fill="both", expand="True")
        miFrame.config(bg="white")
        miFrame.config(width="500",height="400") 
        miFrame.config(bd=39) 
        miFrame.config(relief="groove") 
        miFrame.config(cursor="hand2")
        
        validate_entry = lambda text: text.isdecimal()
        validate_entry2 = lambda text: text.isalpha()
        
        #Etiquetaas
        
        prof=Label(miFrame, text="Registro para Profesores", fg="black")
        prof.pack()
        prof.config(bg="white", relief="flat")
        
        ingresa=Label(miFrame, text="Ingresa los siguientes datos que se solicitan:", fg="black")
        ingresa.pack()
        ingresa.config(bg="white", relief="flat")
        
        nombre=Label(miFrame, text="Nombre:", fg="black")
        nombre.pack()
        nombre.place(x=50, y=60)
        nombre.config(bg="white", relief="flat")
        
        grupo=Label(miFrame, text="Grupo:", fg="black")
        grupo.pack()
        grupo.place(x=50, y=160)
        grupo.config(bg="white", relief="flat")
        
        
        apellidopa=Label(miFrame, text="Apellido Paterno:", fg="black")
        apellidopa.pack()
        apellidopa.place(x=250, y=60)
        apellidopa.config(bg="white", relief="flat")
        
        apellidoma=Label(miFrame, text="Apellido Materno:", fg="black")
        apellidoma.pack()
        apellidoma.place(x=450, y=60)
        apellidoma.config(bg="white", relief="flat")
        
        
        boleta=Label(miFrame, text="Boleta", fg="black")
        boleta.pack()
        boleta.place(x=450, y=160)
        boleta.config(bg="white", relief="flat")
        
        #Cajas de texto 
        
        
        name=Entry(miFrame, highlightthickness=2, )
        name.pack()
        name.place(x=50,y=90)
        name.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        
        apellidopa=Entry(miFrame, highlightthickness=2)
        apellidopa.pack()
        apellidopa.place(x=250,y=90)
        apellidopa.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        apellidom=Entry(miFrame, highlightthickness=2)
        apellidom.pack()
        apellidom.place(x=450,y=90)
        apellidom.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        group=Entry(miFrame, highlightthickness=2)
        group.pack()
        group.place(x=50, y=190)
        group.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        
        nboleta=Entry(miFrame, highlightthickness=2,  validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
        nboleta.pack()
        nboleta.place(x=450, y=190)
        nboleta.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        def botonProfe():
            
            nom=name.get()
            apep=apellidopa.get()
            apem=apellidom.get()
            gru=group.get()
            bo=nboleta.get()
            nom=nom.replace(" ", "")
        
            
            if nom!="" and apep!="" and apem!="" and gru!="" and bo!="":
        
                if len(name.get())<20 and len(apellidopa.get())<15 and len(apellidom.get())<15 and len(group.get())==4 and len(nboleta.get())==10 and nom.isalpha()==True and apep.isalpha()==True and apem.isalpha()==True:
                    tk.messagebox.showinfo("Status","Registro exitoso")
                
                    nombre=name.get()
                    apellidop=apellidopa.get()
                    apellidoma=apellidom.get()
                    boleta=nboleta.get()
                    grupo=group.get()    
                    from Classs import DatosM
                    
                    DatosM=DatosM(nombre.title(),apellidop.title(),apellidoma.title(),boleta,grupo.upper())
                    DatosM.guardar()
                    
                    nombre=name.delete(0, tk.END)
                    apellidop=apellidopa.delete(0, tk.END)
                    apellidoma=apellidom.delete(0, tk.END)
                    boleta=nboleta.delete(0, tk.END)
                    grupo=group.delete(0, tk.END)  
                    from Classs import DatosM
               
        
        butonalum=Button(miFrame, text="Registrar", command=botonProfe)
        butonalum.pack()
        butonalum.place(x=235, y=180)
        
        def consultar():
            archivo=open("archivo.txt","r")
            registros=archivo.read()
            archivo.close()
            messagebox.showinfo("Registros: ", registros)
            
        def retro():
            raiz.destroy()
            from ventana2 import ventanaSele
            ventanaSele.abrirSele()
        
        def salir():
            raiz.destroy()

            
        botonVolver=Button(miFrame, text="Volver", command=retro)
        botonVolver.pack()
        botonVolver.place(x=550, y=280)
        
        botonSalir=Button(miFrame, text="Salir", command=salir)
        botonSalir.place(x=30, y=280)
            
        butonalum=Button(miFrame, text="Mostrar datos", command=consultar)
        butonalum.pack()
        butonalum.place(x=320, y=180)
        
            
        raiz.mainloop()
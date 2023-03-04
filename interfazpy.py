from tkinter import *
import tkinter as tk



raiz=Tk()   
raiz.title("Esta es mi put# ventana") #Titulo de la ventana
raiz.iconbitmap("messi.ico")
raiz.resizable(False,False)
raiz.config(bg="#FFB4A4")

miFrame=Frame() 
miFrame.pack(fill="both", expand="True") 
miFrame.config(bg="white")
miFrame.config(width="400",height="350") #tamaño del frame 
miFrame.config(bd=39)
miFrame.config(relief="groove") 
miFrame.config(cursor="pirate")

usuario=Label(miFrame, text="Usuario", fg="black")
usuario.pack()
usuario.place(x=140, y=50)
usuario.config(bg="white", relief="flat")

cajaus=Entry(miFrame, highlightthickness=2)
cajaus.pack()
cajaus.place(x=100,y=80)
cajaus.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")

passw=Label(miFrame, text="Contraseña", fg="black")
passw.pack()
passw.place(x=128, y=130)
passw.config(bg="white", relief="flat")


cajapass=Entry(miFrame, highlightthickness=2, show="*")
cajapass.pack()
cajapass.place(x=95,y=160)
cajapass.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")

def iniciarsesion():
    caja1=cajaus.get()
    caja2=cajapass.get()
    if caja1=="César" and caja2=="vivaamlo":
        tk.messagebox.showinfo("Status","Haz iniciado sesión, bienvenid@")
        acceso()
    else:
        tk.messagebox.showerror("Status","Usuario y/o contraseña incorrectos")
        caja1=cajaus.delete(0, tk.END)
        caja2=cajapass.delete(0, tk.END)

def acceso():
    raiz.destroy()
    from ventana2 import ventanaSele
    ventanaSele.abrirSele()

butonconfi=Button(miFrame, text="Iniciar sesión")
butonconfi.pack()
butonconfi.place(x=120,y=200)
butonconfi.config(command=iniciarsesion)
#butonconfi.config(bg="#AEFFAA", command= demoColorChange, relief="flat")

def demoColorChange(): butonconfi.configure(bg="#42FF3A")



raiz.mainloop() #Es como un </HTML>
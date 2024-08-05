import tkinter as tk
from tkinter import messagebox
import pyodbc

ventana = tk.Tk()

#-------------------------------------------#
def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")
def VentanaPrncipal():
    ventana.title('Tarea Programada 5')
    ventana.geometry('500x200')
    lblTitulo = tk.Label(ventana, text="Ventana de Login",width=25, justify="center", bd=2, relief="solid", font=("",12))
    lblTitulo.grid(row = 1, column = 1, columnspan=3, padx = 10, pady = 10,sticky="we")

    lblUsuario = tk.Label(ventana, text="Nombre de Usuario: ", width= 20,justify="center", bd=2, relief="solid", font=("",12))
    lblUsuario.grid(row=2, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")

    txtUsuario = tk.Entry(ventana,  width= 20,justify="center", bd=2, relief="solid", font=("",12))
    txtUsuario.grid(row=2, column=2, columnspan=2, padx = 10, pady = 10,sticky="we")
    txtUsuario.focus()

    lblContrasena = tk.Label(ventana, text="Contrasena: ", width= 20,justify="center", bd=2, relief="solid", font=("",12))
    lblContrasena.grid(row=3, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")

    txtContrasena = tk.Entry(ventana,  width= 20,justify="center", bd=2, relief="solid", font=("",12),show='*') # show muestra en el TXT el caracter deseado
    txtContrasena.grid(row=3, column=2, columnspan=2, padx = 10, pady = 10,sticky="we")
    #---------------------------------------------------------------#
    btnLogin = tk.Button(ventana, text="Login",width=10, justify="center", bd=2, relief="solid", font=("",12)) 
    btnLogin.grid(row=4, column= 1, columnspan=1, padx=10, pady= 10, sticky='we' )

    btnLimpiar = tk.Button(ventana, text="Limpiar",width=10, justify="center", bd=2, relief="solid", font=("",12), command=lambda:Limpiar(txtUsuario,txtContrasena))
    btnLimpiar.grid(row=4, column= 2, columnspan=1, padx=10, pady= 10, sticky='we' )

    btnTerminar = tk.Button(ventana, text="Terminar",width=10, justify="center", bd=2, relief="solid", font=("",12), command=ventana.quit)
    btnTerminar.grid(row=4, column= 3, columnspan=1, padx=10, pady= 10, sticky='we' )
#-------------------------------------------#
VentanaPrncipal()
ventana.mainloop()
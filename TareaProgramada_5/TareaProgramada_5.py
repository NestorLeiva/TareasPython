import tkinter as tk
from tkinter import messagebox
import pyodbc

ventana = tk.Tk()
#-------------------------------------------#
def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")
def VentanaLogin():
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

def VentanaSecundaria(ventana):
    nuevaVentana = tk.Toplevel(ventana)
    nuevaVentana.geometry('650x150')
    nuevaVentana.title('Tarea Programada 5')

    lblNombreUsuario = tk.Label(nuevaVentana, text="Usuario:",width=15, justify="center", bd=2, relief="solid", font=("",12))
    lblNombreUsuario.grid(row=0, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")
    
    lblNombreUsuarioRes = tk.Label(nuevaVentana, width=15, justify="center", bd=2, relief="solid", font=("",12))
    lblNombreUsuarioRes.grid(row=0, column=1,  columnspan=1, padx = 5, pady = 5, sticky="we")
    
    lblCodigoUsuarioRes = tk.Label(nuevaVentana, width=15, justify="center", bd=2, relief="solid", font=("",12))
    lblCodigoUsuarioRes.grid(row=0, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")

    lblRolUsuarioRes = tk.Label(nuevaVentana, width=15, justify="center", bd=2, relief="solid", font=("",12))
    lblRolUsuarioRes.grid(row=0, column=3,  columnspan=1, padx = 5, pady = 5, sticky="we")

    lblConsulta = tk.Label(nuevaVentana, text="Que Accion desea Realizar",width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblConsulta.grid(row=3, column=0,  columnspan=4, padx = 5, pady = 5, sticky="we")
    #-------------------------------------------#
    btnCrear = tk.Button(nuevaVentana,text='Ingresar',width=15, justify="center", font=("",12))
    btnCrear.grid(row=4, column=0,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnLeer = tk.Button(nuevaVentana,text='Leer',width=15, justify="center", font=("",12))
    btnLeer.grid(row=4, column=1,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnModificar = tk.Button(nuevaVentana,text='Modificar',width=15, justify="center", font=("",12))
    btnModificar.grid(row=4, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnEliminar = tk.Button(nuevaVentana,text='Eliminar',width=15, justify="center", font=("",12))
    btnEliminar.grid(row=4, column=3,  columnspan=1, padx = 5, pady = 5, sticky="we")


def VentanaCRUD():
    pass
    # Crear /si crea usuario debe de crear login/
    # Leer
    # Actualizar
    # Eliminar /si elimina usuario debe de eliminar login/
#-------------------------------------------#
VentanaLogin()
VentanaSecundaria(ventana)

ventana.mainloop()
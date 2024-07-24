import tkinter as tk
from tkinter import messagebox
import pyodbc


print('version pyodbc',pyodbc.version)
print('version Odbc',pyodbc.drivers())

ventana = tk.Tk()
ventana.title('Tarea Programada 4')
ventana.geometry('550x200')
#---------------------------------------------------------------#
def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")
def NuevaVentana(ventana):
    nuevaVentana = tk.Tk()
    nuevaVentana.geometry('500x300')
    nuevaVentana.title('Tarea Programada: Login')
    #---------------------------------------------------------------#
    lblTituloDatosUsuario = tk.Label(nuevaVentana, text="Datos de Usuario",width=25, justify="center", bd=2, relief="solid", font=("",12))
    lblTituloDatosUsuario.grid(row= 1, column=1, columnspan=2, padx = 10, pady = 10,sticky="we")

    lblCodigo = tk.Label(nuevaVentana, text="Codigo de Usuario",width=25, justify="center", bd=2, relief="solid", font=("",12))
    lblCodigo.grid(row= 2, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")
    
    lblDatosUsuario = tk.Label(nuevaVentana, text="Nombre de Usuario",width=25, justify="center", bd=2, relief="solid", font=("",12))
    lblDatosUsuario.grid(row= 3, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")

    lblContrasenaUsuario = tk.Label(nuevaVentana, text="Contrasena de Usuario",width=25, justify="center", bd=2, relief="solid", font=("",12))
    lblContrasenaUsuario.grid(row= 4, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")

    lblRolUsuario = tk.Label(nuevaVentana, text="",width=25, justify="center", bd=2, relief="solid", font=("",12))
    lblRolUsuario.grid(row= 5, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")
    #---------------------------------------------------------------#
    lblCodigoRes = tk.Label(nuevaVentana, text="",width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblCodigoRes.grid(row= 2, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")
    
    lblDatosUsuarioRes = tk.Label(nuevaVentana, text="",width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblDatosUsuarioRes.grid(row= 3, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")

    lblContrasenaUsuarioRes = tk.Label(nuevaVentana, text="",width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblContrasenaUsuarioRes.grid(row= 4, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")

    lblRolUsuarioRes = tk.Label(nuevaVentana, text="",width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblRolUsuarioRes.grid(row= 5, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")
    #---------------------------------------------------------------#
    btnRegresar = tk.Button(nuevaVentana, text="Regresar",width=25, justify="center", bd=2, relief="solid", font=("",12))
    btnRegresar.grid(row= 6, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")
    SQLConexion()

def SQLConexion():
    usuario = txtUsuario.get()
    contrasena = txtContrasena.get()
    server = "NESTORPC\\NESTOR"
    database = "progra3"
    username = "Nestor"
    password = "nestor123"
    username1 = "Arlin"
    password1 = "arlin123"
    ConexionString = pyodbc.connect( f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;')
    ConexionString1 = pyodbc.connect( f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username1};PWD={password1};TrustServerCertificate=yes;')

    if (usuario == username) and (contrasena == password):
        try:
            conexion = ConexionString
            print("Conexion Exitosa: ", username)
        except pyodbc.Error as e:
            print('Error al realizar la conexion', e)
        finally:
            conexion.close()
            ('se realizo el cierre de la conexion', conexion)
    elif (usuario == username1) and (contrasena == password1):    
        try:
            conexion1 = ConexionString1
            print("Conexion Exitosa: ", username1)
        except pyodbc.Error as e:
            print('Error al realizar la conexion', e)
        finally:
            conexion1.close()
            print('se realizo el cierre de la conexion', conexion1)
    else:
        messagebox.showerror('Tarea Programada 4','Error al realizar la conexion a SQL')
#---------------------------------------------------------------#
lblTitulo = tk.Label(ventana, text="Ventana de Login",width=25, justify="center", bd=2, relief="solid", font=("",12))
lblTitulo.grid(row = 1, column = 1, columnspan=3, padx = 10, pady = 10,sticky="we")

lblUsuario = tk.Label(ventana, text="Nombre de Usuario: ", width= 20,justify="center", bd=2, relief="solid", font=("",12))
lblUsuario.grid(row=2, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")

txtUsuario = tk.Entry(ventana,  width= 20,justify="center", bd=2, relief="solid", font=("",12))
txtUsuario.grid(row=2, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")
txtUsuario.focus()

lblContrasena = tk.Label(ventana, text="Contrasena: ", width= 20,justify="center", bd=2, relief="solid", font=("",12))
lblContrasena.grid(row=3, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")

txtContrasena = tk.Entry(ventana,  width= 20,justify="center", bd=2, relief="solid", font=("",12),show='*') # show muestra en el TXT el caracter deseado
txtContrasena.grid(row=3, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")
#---------------------------------------------------------------#
btnLogin = tk.Button(ventana, text="Login",width=10, justify="center", bd=2, relief="solid", font=("",12), command=lambda:NuevaVentana(ventana))
btnLogin.grid(row=4, column= 1, columnspan=1, padx=10, pady= 10, sticky='we' )

btnLimpiar = tk.Button(ventana, text="Limpiar",width=10, justify="center", bd=2, relief="solid", font=("",12), command=lambda:Limpiar(txtUsuario,txtContrasena))
btnLimpiar.grid(row=4, column= 2, columnspan=1, padx=10, pady= 10, sticky='we' )

btnTerminar = tk.Button(ventana, text="Terminar",width=10, justify="center", bd=2, relief="solid", font=("",12), command=ventana.quit)
btnTerminar.grid(row=4, column= 3, columnspan=1, padx=10, pady= 10, sticky='we' )

#---------------------------------------------------------------#
ventana.mainloop()
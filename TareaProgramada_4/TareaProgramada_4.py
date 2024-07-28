import tkinter as tk
from tkinter import messagebox
import pyodbc

ventana = tk.Tk()
ventana.title('Tarea Programada 4')
ventana.geometry('550x200')

#---------------------------------------------------------------#
def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")

def NuevaVentana(ventana,codigoUsuario, nombreUsuario, contrasenaUsuario, rolUsuario):
    nuevaVentana = tk.Toplevel(ventana) # se configura para que sea una ventana hija de la ventana principal
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

    lblRolUsuario = tk.Label(nuevaVentana, text="Rol de Usuario ",width=25, justify="center", bd=2, relief="solid", font=("",12))
    lblRolUsuario.grid(row= 5, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")
    #---------------------------------------------------------------#
    lblCodigoRes = tk.Label(nuevaVentana,text='', width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblCodigoRes.grid(row= 2, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")
    
    lblDatosUsuarioRes = tk.Label(nuevaVentana, width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblDatosUsuarioRes.grid(row= 3, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")

    lblContrasenaUsuarioRes = tk.Label(nuevaVentana, width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblContrasenaUsuarioRes.grid(row= 4, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")

    lblRolUsuarioRes = tk.Label(nuevaVentana, width=25, justify="left", bd=2, relief="solid", font=("",12))
    lblRolUsuarioRes.grid(row= 5, column=2, columnspan=1, padx = 10, pady = 10,sticky="we")
    #---------------------------------------------------------------#
    btnRegresar = tk.Button(nuevaVentana, text="Regresar",width=25, justify="center", bd=2, relief="solid", font=("",12), command= nuevaVentana.destroy) # cierra la vetana
    btnRegresar.grid(row= 6, column=1, columnspan=1, padx = 10, pady = 10,sticky="we")
    #---------------------------------------------------------------#
    lblCodigoRes.config(text=codigoUsuario)
    lblDatosUsuarioRes.config(text=nombreUsuario)
    lblContrasenaUsuarioRes.config(text=contrasenaUsuario)
    lblRolUsuarioRes.config(text=rolUsuario)
    # obtengo los valores de la consulta  y los imprimo en los label. los valores los obtengo de los parametros de la funcion

def SQLConexion():
    usuario = txtUsuario.get()
    contrasena = txtContrasena.get()
    server = "NESTORPC\\NESTOR"
    database = "prograIII"   
    if usuario.strip() and contrasena.strip():
        ConexionString = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={usuario};PWD={contrasena};TrustServerCertificate=yes;')
        try:
            conexion = ConexionString
            print("Conexion Exitosa: ", usuario)
            messagebox.showinfo('Tarea Programada 4', f'Login Exitoso: {usuario}')
            RealizarConsulta(conexion, usuario, ventana)
        except pyodbc.Error as e:
            print('Error al realizar la conexion', e)
            messagebox.showerror('Tarea Programada 4', 'Error al realizar la conexion')
        finally:
            conexion.close()
            print('se realizo el cierre de la conexion',usuario)
            return True # Devuelve True si la conexión y autenticación fueron exitosas
    else:
        messagebox.showerror('Tarea Programada 4','Error al realizar la conexion a SQL')
        return False # Devuelve False si hubo un error en la conexión

def RealizarConsulta(conexion, usuario, ventana):
    try:
        consulta = conexion.cursor()
        query = """ SELECT Usuarios.Codigo, Usuarios.Usuario, Usuarios.Contra, Roles.Descripcion_rol
                FROM Usuarios
                INNER JOIN Roles ON Usuarios.Rol = Roles.Rol
                INNER JOIN Estados ON Usuarios.Estado = Estados.Estado
                WHERE Usuarios.Usuario = ? """
        print(f'Ejecutando Consulta: {usuario}')
        consulta.execute(query, (usuario,))
        for row in consulta:
            print('Consulta: ',row)
            NuevaVentana(ventana, row[0],row[1],row[2],row[3],) # pinto los datos obtenidos en el orden especificado
    except pyodbc.Error as e:
        print('Error al realizar la consulta', e)
        messagebox.showerror('Tarea Programada 4','Error al realizar la consulta')
    finally:
        consulta.close()

def NuevoLogin():
    SQLConexion() # funcion que valida la conexion SQL si es Valida muesta la Ventana
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
btnLogin = tk.Button(ventana, text="Login",width=10, justify="center", bd=2, relief="solid", font=("",12), command=NuevoLogin) 
btnLogin.grid(row=4, column= 1, columnspan=1, padx=10, pady= 10, sticky='we' )

btnLimpiar = tk.Button(ventana, text="Limpiar",width=10, justify="center", bd=2, relief="solid", font=("",12), command=lambda:Limpiar(txtUsuario,txtContrasena))
btnLimpiar.grid(row=4, column= 2, columnspan=1, padx=10, pady= 10, sticky='we' )

btnTerminar = tk.Button(ventana, text="Terminar",width=10, justify="center", bd=2, relief="solid", font=("",12), command=ventana.quit)
btnTerminar.grid(row=4, column= 3, columnspan=1, padx=10, pady= 10, sticky='we' )
#---------------------------------------------------------------#
ventana.mainloop()
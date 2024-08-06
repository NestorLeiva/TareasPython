import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import SQLConexion
import MetodosSQL

ventana = tk.Tk()
#-------------------------------------------#
def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")

def AceptarCambios():
    print(messagebox.askyesno(message="¿Desea Continuar?", title="Tarea Programada 5"))


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
    btnCrear = tk.Button(nuevaVentana,text='Ingresar',width=15, justify="center", font=("",12), command=VentanaCrear)
    btnCrear.grid(row=4, column=0,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnLeer = tk.Button(nuevaVentana,text='Leer',width=15, justify="center", font=("",12), command=VentanaLeer)
    btnLeer.grid(row=4, column=1,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnModificar = tk.Button(nuevaVentana,text='Modificar',width=15, justify="center", font=("",12), command=VentanaModificar)
    btnModificar.grid(row=4, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnEliminar = tk.Button(nuevaVentana,text='Eliminar',width=15, justify="center", font=("",12), command=VentanaEliminar)
    btnEliminar.grid(row=4, column=3,  columnspan=1, padx = 5, pady = 5, sticky="we")

def VentanaCrear():
    Ventana_Crear = tk.Toplevel(ventana)
    Ventana_Crear.geometry('600x350')
    Ventana_Crear.title('Ingreso de Usuario')
    
    # codigo aumentado automaticamente
    lblUsuario = tk.Label(Ventana_Crear, text="Nombre de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblUsuario.grid(row=0, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblContrasenaUsuario = tk.Label(Ventana_Crear, text="Contrasena de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblContrasenaUsuario.grid(row=1, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblNombreUsuario = tk.Label(Ventana_Crear, text="Nombre:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblNombreUsuario.grid(row=2, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblRolUsuario = tk.Label(Ventana_Crear, text="Rol del Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblRolUsuario.grid(row=3, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblEstadoUsuario = tk.Label(Ventana_Crear, text="Estado del Usuario:",width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblEstadoUsuario.grid(row=4, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    txtUsuario = tk.Entry(Ventana_Crear, width=20, justify="center", bd=2, relief="solid", font=("",12))
    txtUsuario.grid(row=0, column=1,  columnspan=1, padx = 10, pady = 10, sticky="we")
    txtUsuario.focus()
 
    txtContrasenaUsuario = tk.Entry(Ventana_Crear, width=20, justify="center", bd=2, relief="solid", font=("",12),show='*')
    txtContrasenaUsuario.grid(row=1, column=1,  columnspan=1, padx = 10, pady = 10, sticky="we")

    txtNombreUsuario = tk.Entry(Ventana_Crear, width=20, justify="center", bd=2, relief="solid", font=("",12))
    txtNombreUsuario.grid(row=2, column=1,  columnspan=1, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    cboRolUsuario = ttk.Combobox(Ventana_Crear, state="readonly", font=("", 12), values= ('Administrador????', 'Usuario????', 'Invitado????'))
    cboRolUsuario.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="we")

    cboEstadoUsuario = ttk.Combobox(Ventana_Crear, state="readonly", font=("", 12), values= ('Activo', 'InActivo'))
    cboEstadoUsuario.grid(row=4, column=1,  columnspan=1, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    btnGuardar = tk.Button(Ventana_Crear, text='Guardar', width=15, justify="center", font=("",12), command=AceptarCambios)
    btnGuardar.grid(row=5, column=0,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnLimpiar = tk.Button(Ventana_Crear, text='Limpiar', width=15, justify="center", font=("",12), command=lambda: Limpiar(txtUsuario,txtContrasenaUsuario,txtNombreUsuario))
    btnLimpiar.grid(row=5, column=1,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnCancelar = tk.Button(Ventana_Crear, text='Cancelar', width=15, justify="center", font=("",12), command= Ventana_Crear.destroy)
    btnCancelar.grid(row=5, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")

def VentanaLeer():
    Nueva_Leer = tk.Toplevel(ventana)
    Nueva_Leer.geometry('650x500')
    Nueva_Leer.title('Mostrar Datos Usuarios')
    lblNombreUsuario = tk.Label(Nueva_Leer, text="Ventana Leer:",width=15, justify="center", bd=2, relief="solid", font=("",12))
    lblNombreUsuario.grid(row=0, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

def VentanaModificar():
    Ventana_Modificar = tk.Toplevel(ventana)
    Ventana_Modificar.geometry('600x350')
    Ventana_Modificar.title('Modificacion de Usuarios')
    
    lblBuscarUsuario = tk.Label(Ventana_Modificar, text="Buscar Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblBuscarUsuario.grid(row=0, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    txtBuscarUsuario = tk.Entry(Ventana_Modificar, width=20, justify="center", bd=2, relief="solid", font=("",12))
    txtBuscarUsuario.grid(row=0, column=1,  columnspan=1, padx = 10, pady = 10, sticky="we")
    txtBuscarUsuario.focus()

    btnBuscarUsuario = tk.Button(Ventana_Modificar, text='Buscar', width=15, justify="center", font=("",12))
    btnBuscarUsuario.grid(row=0, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")
    #-------------------------------------------#
    lblUsuario = tk.Label(Ventana_Modificar, text="Nombre de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblUsuario.grid(row=1, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblContrasenaUsuario = tk.Label(Ventana_Modificar, text="Contrasena de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblContrasenaUsuario.grid(row=2, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblNombreUsuario = tk.Label(Ventana_Modificar, text="Nombre:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblNombreUsuario.grid(row=3, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblRolUsuario = tk.Label(Ventana_Modificar, text="Rol del Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblRolUsuario.grid(row=4, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblEstadoUsuario = tk.Label(Ventana_Modificar, text="Estado del Usuario:",width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblEstadoUsuario.grid(row=5, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    txtUsuario = tk.Entry(Ventana_Modificar, width=20, justify="center", bd=2, relief="solid", font=("",12))
    txtUsuario.grid(row=1, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")
  
    txtContrasenaUsuario = tk.Entry(Ventana_Modificar, width=20, justify="center", bd=2, relief="solid", font=("",12),show='*')
    txtContrasenaUsuario.grid(row=2, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")

    txtNombreUsuario = tk.Entry(Ventana_Modificar, width=20, justify="center", bd=2, relief="solid", font=("",12))
    txtNombreUsuario.grid(row=3, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    cboRolUsuario = ttk.Combobox(Ventana_Modificar, state="readonly", font=("", 12), values= ('Administrador????', 'Usuario????', 'Invitado????'))
    cboRolUsuario.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="we")

    cboEstadoUsuario = ttk.Combobox(Ventana_Modificar, state="readonly", font=("", 12), values= ('Activo', 'InActivo'))
    cboEstadoUsuario.grid(row=5, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    btnGuardar = tk.Button(Ventana_Modificar, text='Guardar', width=15, justify="center", font=("",12), command= AceptarCambios)
    btnGuardar.grid(row=6, column=0,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnLimpiar = tk.Button(Ventana_Modificar, text='Limpiar', width=15, justify="center", font=("",12), command=lambda: Limpiar(txtUsuario,txtContrasenaUsuario,txtNombreUsuario))
    btnLimpiar.grid(row=6, column=1,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnCancelar = tk.Button(Ventana_Modificar, text='Cancelar', width=15, justify="center", font=("",12), command= Ventana_Modificar.destroy)
    btnCancelar.grid(row=6, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")

def VentanaEliminar():
    Ventana_Eliminar = tk.Toplevel(ventana)
    Ventana_Eliminar.geometry('600x350')
    Ventana_Eliminar.title('Eliminar Usuario')

    lblBuscarUsuario = tk.Label(Ventana_Eliminar, text="Buscar Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblBuscarUsuario.grid(row=0, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    txtBuscarUsuario = tk.Entry(Ventana_Eliminar, width=20, justify="center", bd=2, relief="solid", font=("",12))
    txtBuscarUsuario.grid(row=0, column=1,  columnspan=1, padx = 10, pady = 10, sticky="we")
    txtBuscarUsuario.focus()

    btnBuscarUsuario = tk.Button(Ventana_Eliminar, text='Buscar', width=15, justify="center", font=("",12))
    btnBuscarUsuario.grid(row=0, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")
    #-------------------------------------------#
    lblUsuario = tk.Label(Ventana_Eliminar, text="Nombre de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblUsuario.grid(row=1, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblContrasenaUsuario = tk.Label(Ventana_Eliminar, text="Contrasena de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblContrasenaUsuario.grid(row=2, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblNombreUsuario = tk.Label(Ventana_Eliminar, text="Nombre:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblNombreUsuario.grid(row=3, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblRolUsuario = tk.Label(Ventana_Eliminar, text="Rol del Usuario:", width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblRolUsuario.grid(row=4, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")

    lblEstadoUsuario = tk.Label(Ventana_Eliminar, text="Estado del Usuario:",width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblEstadoUsuario.grid(row=5, column=0,  columnspan=1, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    lblUsuarioRes = tk.Label(Ventana_Eliminar, width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblUsuarioRes.grid(row=1, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")
  
    lblContrasenaRes = tk.Label(Ventana_Eliminar, width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblContrasenaRes.grid(row=2, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")

    lblNombreUsuarioRes = tk.Label(Ventana_Eliminar, width=20, justify="center", bd=2, relief="solid", font=("",12))
    lblNombreUsuarioRes.grid(row=3, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    cboRolUsuario = ttk.Combobox(Ventana_Eliminar, state="readonly", font=("", 12), values= ('Administrador????', 'Usuario????', 'Invitado????'))
    cboRolUsuario.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="we")

    lblEstadoUsuarioRes = ttk.Combobox(Ventana_Eliminar, state="readonly", font=("", 12), values= ('Activo', 'InActivo'))
    lblEstadoUsuarioRes.grid(row=5, column=1,  columnspan=2, padx = 10, pady = 10, sticky="we")
    #-------------------------------------------#
    btnAceptar = tk.Button(Ventana_Eliminar, text='Aceptar', width=15, justify="center", font=("",12), command=AceptarCambios)
    btnAceptar.grid(row=6, column=1,  columnspan=1, padx = 5, pady = 5, sticky="we")

    btnCancelar = tk.Button(Ventana_Eliminar, text='Cancelar', width=15, justify="center", font=("",12), command= Ventana_Eliminar.destroy)
    btnCancelar.grid(row=6, column=2,  columnspan=1, padx = 5, pady = 5, sticky="we")

#-------------------------------------------#
VentanaLogin()
VentanaSecundaria(ventana)


ventana.mainloop()
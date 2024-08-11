import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import SQLConexion

ventana = tk.Tk()
# ---------------------------------------------------------------------------------------------------------------------------------#
def Limpiar(*TextoWidget):
    for texto in TextoWidget:
        texto.delete(0, "end")
# -------------------------------------------#
def Insertar():
    VentanaCrear(CodigoMovimiento = 1)
def Modifico():
    VentanaModificar(CodigoMovimiento = 2)
def Elimino():
    VentanaEliminar(CodigoMovimiento = 3)
def Leer():
     VentanaLeer(CodigoMovimiento = 4)
# -------------------------------------------#
def login(usuario, contrasena):
    if SQLConexion.Conexion.LoginSQL(usuario, contrasena) == True:
        ventana.withdraw()  # oculta la ventana
        VentanaSecundaria(ventana)
        # los parametros son las variables globales que estan definidas en def VentanaLogin()
        Limpiar(txtUsuario, txtContrasena)
    else:
        Limpiar(txtUsuario, txtContrasena)
    """ valida que LoginSQL sea True, si lo es abre la ventana secundaria. """
# Metodo para ingresar al programa y validar las credenciales
def CerrarSesion(ventana, nuevaVentana):
    SQLConexion.Conexion.CerrarSQL()  # llamo al metodo de la clase
    nuevaVentana.destroy()
    ventana.deiconify()  # muestra la ventana
# Cierro la sesion de la Base Datos. y muestra la ventana Login
def InsertUsuario(txtCodigoUsuarioC,txtUsuarioC, txtContrasenaUsuarioC,txtNombreUsuarioC,cboRolUsuarioC,cboEstadoUsuarioC,CodigoMovimiento):
    codigo = txtCodigoUsuarioC.get().strip()
    usuario = txtUsuarioC.get().strip()
    contrasena = txtContrasenaUsuarioC.get().strip()
    nombre = txtNombreUsuarioC.get().strip()
    rol = cboRolUsuarioC.current() + 1 # índice del combo inicia en 0, por lo que sumamos 1
    estado = cboEstadoUsuarioC.current() + 1
    SQLConexion.MetodosSQL.EscribirSQL(codigo,usuario,contrasena, nombre,rol,estado,CodigoMovimiento)
    Limpiar(txtCodigoUsuarioC,txtUsuarioC, txtContrasenaUsuarioC,txtNombreUsuarioC)
# Metodo para Insertar datos Usuario a BD
def MetodoModificar(codigoM,txtUsuario,txtContrasenaUsuario,txtNombreUsuario,cboRolUsuario,cboEstadoUsuario, CodigoMovimiento):
    codigo = codigoM.get()
    usuario = txtUsuario.get().strip()
    contrasena = txtContrasenaUsuario.get().strip()
    nombre = txtNombreUsuario.get().strip()
    rol = cboRolUsuario.current() + 1 
    estado = cboEstadoUsuario.current() + 1
    SQLConexion.MetodosSQL.ModificarSQL(codigo, usuario, contrasena, nombre, rol, estado, CodigoMovimiento)
#Metodo para Modificar Usuario de BD
def BuscarUsuario(codigo,txtUsuario, txtContrasenaUsuario, txtNombreUsuario, cboRolUsuario, cboEstadoUsuario):
    try:
        if codigo.isdigit():
            codigo = int(codigo)
            datos = SQLConexion.MetodosSQL.ConsultaSQL(codigo)
            if datos:  # Valido si la consulta tiene datos almacenados
                for dato in datos:
                    txtUsuario.delete(0, tk.END)
                    txtUsuario.insert(0, dato[1])
                    txtContrasenaUsuario.delete(0, tk.END)
                    txtContrasenaUsuario.insert(0, dato[2])
                    txtNombreUsuario.delete(0, tk.END)
                    txtNombreUsuario.insert(0, dato[3])
                    cboRolUsuario.set(dato[4])
                    cboEstadoUsuario.set(dato[5])
            else:
                Limpiar( txtUsuario, txtContrasenaUsuario, txtNombreUsuario)
        else:
            messagebox.showwarning('Tarea Programada 5', 'El Codigo del usuario solo debe de ser Numerico')
    except: 
        messagebox.showerror('Tarea Programada 5', 'Codigo de Usuario no Existe')
# metodo para realizar la Busqueda del usuario

# ---------------------------------------------------------------------------------------------------------------------------------#
def VentanaLogin():
    ventana.title('Tarea Programada 5')
    ventana.geometry('500x200')

    global txtUsuario, txtContrasena  # variables globales

    lblTitulo = tk.Label(ventana, text="Ventana de Login", width=25,justify="center", bd=2, relief="solid", font=("", 12))
    lblTitulo.grid(row=1, column=1, columnspan=3,padx=10, pady=10, sticky="we")

    lblUsuario = tk.Label(ventana, text="Nombre de Usuario: ", width=20,justify="center", bd=2, relief="solid", font=("", 12))
    lblUsuario.grid(row=2, column=1, columnspan=1,padx=10, pady=10, sticky="we")

    txtUsuario = tk.Entry(ventana,  width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtUsuario.grid(row=2, column=2, columnspan=2,padx=10, pady=10, sticky="we")
    txtUsuario.focus()

    lblContrasena = tk.Label(ventana, text="Contrasena: ", width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblContrasena.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="we")

    txtContrasena = tk.Entry(ventana,  width=20, justify="center", bd=2, relief="solid", font=("", 12), show='*')
    txtContrasena.grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky="we")
    # ---------------------------------------------------------------#
    btnLogin = tk.Button(ventana, text="Login", width=10, justify="center", bd=2, relief="solid", font=("", 12), command=lambda: login(txtUsuario.get().strip(), txtContrasena.get().strip()))
    btnLogin.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky='we')

    btnLimpiar = tk.Button(ventana, text="Limpiar", width=10, justify="center", bd=2, relief="solid", font=("", 12), command=lambda: Limpiar(txtUsuario, txtContrasena))
    btnLimpiar.grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky='we')

    btnTerminar = tk.Button(ventana, text="Terminar", width=10, justify="center", bd=2, relief="solid", font=("", 12), command=ventana.quit)
    btnTerminar.grid(row=4, column=3, columnspan=1, padx=10, pady=10, sticky='we')
# ventana Principal
def VentanaSecundaria(ventana):
    nuevaVentana = tk.Toplevel(ventana)
    nuevaVentana.geometry('650x200')
    nuevaVentana.title('Tarea Programada 5')

    lblConsulta = tk.Label(nuevaVentana, text="Que Accion desea Realizar", width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblConsulta.grid(row=3, column=0,  columnspan=4, padx=5, pady=5, sticky="we")

    btnCrear = tk.Button(nuevaVentana, text='Ingresar', width=15, justify="center", font=("", 12), command=Insertar)
    btnCrear.grid(row=4, column=0,  columnspan=1, padx=5, pady=5, sticky="we")

    btnLeer = tk.Button(nuevaVentana, text='Leer', width=15, justify="center", font=("", 12), command=Leer)
    btnLeer.grid(row=4, column=1,  columnspan=1, padx=5, pady=5, sticky="we")

    btnModificar = tk.Button(nuevaVentana, text='Modificar', width=15,  justify="center", font=("", 12), command=Modifico)
    btnModificar.grid(row=4, column=2,  columnspan=1, padx=5, pady=5, sticky="we")

    btnEliminar = tk.Button(nuevaVentana, text='Eliminar', width=15, justify="center", font=("", 12), command=Elimino)
    btnEliminar.grid(row=4, column=3,  columnspan=1, padx=5, pady=5, sticky="we")

    btnCerrarSesion = tk.Button(nuevaVentana, text="Cerrar Sesion", width=10, justify="center", bd=2, font=("", 12), command=lambda: CerrarSesion(ventana, nuevaVentana))
    btnCerrarSesion.grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky='we')
# ventana Secundaria
def VentanaCrear(CodigoMovimiento=None):
    Ventana_Crear = tk.Toplevel(ventana)
    Ventana_Crear.geometry('600x350')
    Ventana_Crear.title('Ingreso de Usuario')
    
    global txtCodigoUsuarioC ,txtUsuarioC, txtContrasenaUsuarioC, txtNombreUsuarioC, cboRolUsuarioC, cboEstadoUsuarioC
    
    lblCodigoUsuario = tk.Label(Ventana_Crear, text="Codigo de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblCodigoUsuario.grid(row=0, column=0,  columnspan=1, padx=10, pady=10, sticky="we")

    lblUsuario = tk.Label(Ventana_Crear, text="Nombre de Usuario:", width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblUsuario.grid(row=1, column=0,  columnspan=1, padx=10, pady=10, sticky="we")

    lblContrasenaUsuario = tk.Label(Ventana_Crear, text="Contrasena de Usuario:",  width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblContrasenaUsuario.grid(row=2, column=0,  columnspan=1, padx=10, pady=10, sticky="we")

    lblNombreUsuario = tk.Label(Ventana_Crear, text="Nombre y Apellido:",  width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblNombreUsuario.grid(row=3, column=0,  columnspan=1, padx=10, pady=10, sticky="we")

    lblRolUsuario = tk.Label(Ventana_Crear, text="Rol del Usuario:", width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblRolUsuario.grid(row=4, column=0,  columnspan=1,  padx=10, pady=10, sticky="we")

    lblEstadoUsuario = tk.Label(Ventana_Crear, text="Estado del Usuario:", width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblEstadoUsuario.grid(row=5, column=0,  columnspan=1, padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    txtCodigoUsuarioC = tk.Entry(Ventana_Crear, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtCodigoUsuarioC.grid(row=0, column=1,  columnspan=1,  padx=10, pady=10, sticky="we")
    txtCodigoUsuarioC.focus()

    txtUsuarioC = tk.Entry(Ventana_Crear, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtUsuarioC.grid(row=1, column=1,  columnspan=1,  padx=10, pady=10, sticky="we")
    
    txtContrasenaUsuarioC = tk.Entry(Ventana_Crear, width=20, justify="center", bd=2, relief="solid", font=("", 12), show='*')
    txtContrasenaUsuarioC.grid(row=2, column=1,  columnspan=1, padx=10, pady=10, sticky="we")

    txtNombreUsuarioC = tk.Entry(Ventana_Crear, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtNombreUsuarioC.grid(row=3, column=1,  columnspan=1,padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    cboRolUsuarioC = ttk.Combobox(Ventana_Crear, state="readonly", font=("", 12), values=(['Admin', 'Conta','Supervisor','Operario']))
    cboRolUsuarioC.grid(row=4, column=1, columnspan=1,padx=10, pady=10, sticky="we")

    cboEstadoUsuarioC = ttk.Combobox(Ventana_Crear, state="readonly", font=("", 12),values=(['Activo', 'InActivo']))
    cboEstadoUsuarioC.grid(row=5, column=1,  columnspan=1,padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    btnGuardar = tk.Button(Ventana_Crear, text='Guardar',width=15, justify="center", font=("", 12), command=lambda: 
                           InsertUsuario(txtCodigoUsuarioC, txtUsuarioC, txtContrasenaUsuarioC,txtNombreUsuarioC,
                                         cboRolUsuarioC,cboEstadoUsuarioC, CodigoMovimiento) )
    btnGuardar.grid(row=6, column=0,  columnspan=1,padx=5, pady=5, sticky="we")

    btnLimpiar = tk.Button(Ventana_Crear, text='Limpiar', width=15, justify="center", font=("", 12), command=lambda: Limpiar(txtUsuarioC, txtContrasenaUsuarioC, txtNombreUsuarioC))
    btnLimpiar.grid(row=6, column=1,  columnspan=1,padx=5, pady=5, sticky="we")

    btnCancelar = tk.Button(Ventana_Crear, text='Cancelar', width=15,justify="center", font=("", 12), command=Ventana_Crear.destroy)
    btnCancelar.grid(row=7, column=1,  columnspan=1,padx=5, pady=5, sticky="we")
# ventana Ingresar Usuarios
def VentanaLeer(CodigoMovimiento=None):
    Ventana_Leer = tk.Toplevel(ventana)
    Ventana_Leer.geometry('800x500')
    Ventana_Leer.title('Mostrar Datos Usuarios')

    Ventana_Leer.grid_rowconfigure(1, weight=1)
    Ventana_Leer.grid_columnconfigure(0, weight=1)

    lblConsulta = tk.Label(Ventana_Leer, text="Datos de los Usuarios", width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblConsulta.grid(row=0, column=0, columnspan=4,padx=5, pady=5, sticky="we")

    TablaUsuarios = ttk.Treeview(Ventana_Leer, columns=('Codigo', 'Usuario','Contra', 'Nombre', 'Rol', 'Estado'), show="headings")
    TablaUsuarios.heading("Codigo", text="Codigo")
    TablaUsuarios.heading("Usuario", text="Usuario")
    TablaUsuarios.heading("Contra", text="Contrasena")
    TablaUsuarios.heading("Nombre", text="Nombre")
    TablaUsuarios.heading("Rol", text="Rol")
    TablaUsuarios.heading("Estado", text="Estado")
    TablaUsuarios.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def ConsultaUsuarios():
        try:
            for items in TablaUsuarios.get_children():  # obtengo todos los elementos de la tabla
                TablaUsuarios.delete(items)
            # se eliminan los datos de la tabla
            ResConsulta = SQLConexion.MetodosSQL.LeerUsuariosSQL(SQLConexion.Conexion.conn )
            for fila in ResConsulta:
                TablaUsuarios.insert("", "end", values=fila)
                # se imprimen los datos en la Tabla
            if ResConsulta:
                usuario = ResConsulta[0][0]
                SQLConexion.MetodosSQL.Auditoria(usuario, CodigoMovimiento) # obtengo el CodigoUsuario  y lo paso a def Auditoria
            else:
                print('No hay Usuario para Registrar la Auditoria')
            
        except:
            messagebox.showerror('Tarea Programda 5', 'Error al Cargar la Lista de Usuarios')
            print('Error al imprimir la tabla y agregar los datos Auditoria')

    def ajustar_columnas(event):
        total_width = event.width
        num_cols = len(TablaUsuarios['columns'])
        col_width = total_width // num_cols
        for col in TablaUsuarios['columns']:
            TablaUsuarios.column(col, width=col_width)
    #  calcula el ancho de cada columna de la Treeview y el número de columnas. ajusta el ancho de cada columna
    
    Ventana_Leer.bind('<Configure>', ajustar_columnas)
    ConsultaUsuarios()
    btnActualizar = tk.Button(Ventana_Leer, text='Actualizar', width=15, justify="center", font=("", 12), command=lambda: ConsultaUsuarios())
    btnActualizar.grid(row=2, column=1,  columnspan=1, padx=5, pady=5, sticky="we")

    btnCancelar = tk.Button(Ventana_Leer, text='Cancelar', width=15,justify="center", font=("", 12), command=Ventana_Leer.destroy)
    btnCancelar.grid(row=2, column=2,  columnspan=1,padx=5, pady=5, sticky="we")
# ventana Ver lista Usuarios
def VentanaModificar(CodigoMovimiento=None):
    Ventana_Modificar = tk.Toplevel(ventana)
    Ventana_Modificar.geometry('600x350')
    Ventana_Modificar.title('Modificacion de Usuarios')

    lblBuscarUsuario = tk.Label(Ventana_Modificar, text="Buscar Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblBuscarUsuario.grid(row=0, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    txtBuscarUsuarioM = tk.Entry(Ventana_Modificar, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtBuscarUsuarioM.grid(row=0, column=1,  columnspan=1,padx=10, pady=10, sticky="we")
    txtBuscarUsuarioM.focus()

    btnBuscarUsuario = tk.Button(Ventana_Modificar, text='Buscar', width=15, justify="center", font=("", 12), 
                                 command=lambda: BuscarUsuario(txtBuscarUsuarioM.get().strip(),
                                                               txtUsuario, txtContrasenaUsuario, txtNombreUsuario, cboRolUsuario, cboEstadoUsuario))
    btnBuscarUsuario.grid(row=0, column=2,  columnspan=1,padx=5, pady=5, sticky="we")
    # -------------------------------------------#
    lblUsuario = tk.Label(Ventana_Modificar, text="Nombre de Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblUsuario.grid(row=1, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    lblContrasenaUsuario = tk.Label(Ventana_Modificar, text="Contrasena de Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblContrasenaUsuario.grid(row=2, column=0,  columnspan=1, padx=10, pady=10, sticky="we")

    lblNombreUsuario = tk.Label(Ventana_Modificar, text="Nombre:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblNombreUsuario.grid(row=3, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    lblRolUsuario = tk.Label(Ventana_Modificar, text="Rol del Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblRolUsuario.grid(row=4, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    lblEstadoUsuario = tk.Label(Ventana_Modificar, text="Estado del Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblEstadoUsuario.grid(row=5, column=0,  columnspan=1,padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    txtUsuario = tk.Entry(Ventana_Modificar, width=20,justify="center", bd=2, relief="solid", font=("", 12))
    txtUsuario.grid(row=1, column=1,  columnspan=2,padx=10, pady=10, sticky="we")

    txtContrasenaUsuario = tk.Entry(Ventana_Modificar, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtContrasenaUsuario.grid(row=2, column=1,  columnspan=2, padx=10, pady=10, sticky="we")

    txtNombreUsuario = tk.Entry(Ventana_Modificar, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtNombreUsuario.grid(row=3, column=1,  columnspan=2,padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    cboRolUsuario = ttk.Combobox(Ventana_Modificar, state="readonly", font=("", 12), values=(['Admin', 'Conta','Supervisor','Operario']))
    cboRolUsuario.grid(row=4, column=1, columnspan=2,padx=10, pady=10, sticky="we")

    cboEstadoUsuario = ttk.Combobox(Ventana_Modificar, state="readonly", font=("", 12), values=('Activo', 'InActivo'))
    cboEstadoUsuario.grid(row=5, column=1,  columnspan=2,padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    btnGuardar = tk.Button(Ventana_Modificar, text='Guardar',width=15, justify="center", font=("", 12), 
                           command=lambda: 
                           MetodoModificar(txtBuscarUsuarioM, txtUsuario, txtContrasenaUsuario, txtNombreUsuario, cboRolUsuario, cboEstadoUsuario, CodigoMovimiento))
    btnGuardar.grid(row=6, column=0,  columnspan=1,padx=5, pady=5, sticky="we")

    btnLimpiar = tk.Button(Ventana_Modificar, text='Limpiar', width=15, justify="center", font=("", 12), command=lambda: Limpiar(txtUsuario, txtContrasenaUsuario, txtNombreUsuario))
    btnLimpiar.grid(row=6, column=1,  columnspan=1,padx=5, pady=5, sticky="we")

    btnCancelar = tk.Button(Ventana_Modificar, text='Cancelar', width=15,justify="center", font=("", 12), command=Ventana_Modificar.destroy)
    btnCancelar.grid(row=6, column=2,  columnspan=1,padx=5, pady=5, sticky="we")
# ventana para modificar datos Usuarios
def VentanaEliminar(CodigoMovimiento=None):
    Ventana_Eliminar = tk.Toplevel(ventana)
    Ventana_Eliminar.geometry('600x350')
    Ventana_Eliminar.title('Eliminar Usuario')
    
    lblBuscarUsuario = tk.Label(Ventana_Eliminar, text="Buscar Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblBuscarUsuario.grid(row=0, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    txtBuscarUsuarioE = tk.Entry(Ventana_Eliminar, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtBuscarUsuarioE.grid(row=0, column=1,  columnspan=1,padx=10, pady=10, sticky="we")
    txtBuscarUsuarioE.focus()

    btnBuscarUsuario = tk.Button(Ventana_Eliminar, text='Buscar', width=15, justify="center", font=("", 12), 
                                command=lambda: BuscarUsuario(txtBuscarUsuarioE.get().strip(),
                                                            txtUsuario, txtContrasenaUsuario, txtNombreUsuario, cboRolUsuario, cboEstadoUsuario))
    btnBuscarUsuario.grid(row=0, column=2,  columnspan=1,padx=5, pady=5, sticky="we")
    # -------------------------------------------#
    lblUsuario = tk.Label(Ventana_Eliminar, text="Nombre de Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblUsuario.grid(row=1, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    lblContrasenaUsuario = tk.Label(Ventana_Eliminar, text="Contrasena de Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblContrasenaUsuario.grid(row=2, column=0,  columnspan=1, padx=10, pady=10, sticky="we")

    lblNombreUsuario = tk.Label(Ventana_Eliminar, text="Nombre:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblNombreUsuario.grid(row=3, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    lblRolUsuario = tk.Label(Ventana_Eliminar, text="Rol del Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblRolUsuario.grid(row=4, column=0,  columnspan=1,padx=10, pady=10, sticky="we")

    lblEstadoUsuario = tk.Label(Ventana_Eliminar, text="Estado del Usuario:",width=20, justify="center", bd=2, relief="solid", font=("", 12))
    lblEstadoUsuario.grid(row=5, column=0,  columnspan=1,padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    txtUsuario = tk.Entry(Ventana_Eliminar, width=20,justify="center", bd=2, relief="solid", font=("", 12))
    txtUsuario.grid(row=1, column=1,  columnspan=2,padx=10, pady=10, sticky="we")

    txtContrasenaUsuario = tk.Entry(Ventana_Eliminar, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtContrasenaUsuario.grid(row=2, column=1,  columnspan=2,padx=10, pady=10, sticky="we")

    txtNombreUsuario = tk.Entry(Ventana_Eliminar, width=20, justify="center", bd=2, relief="solid", font=("", 12))
    txtNombreUsuario.grid(row=3, column=1,  columnspan=2, padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    cboRolUsuario = ttk.Combobox(Ventana_Eliminar, state="readonly", font=("", 12), values=(['Admin', 'Conta','Supervisor','Operario']))
    cboRolUsuario.grid(row=4, column=1, columnspan=2,padx=10, pady=10, sticky="we")

    cboEstadoUsuario = ttk.Combobox(Ventana_Eliminar, state="readonly", font=("", 12), values=('Activo', 'InActivo'))
    cboEstadoUsuario.grid(row=5, column=1,  columnspan=2, padx=10, pady=10, sticky="we")
    # -------------------------------------------#
    cod_eliminar = txtBuscarUsuarioE
    btnEliminar = tk.Button(Ventana_Eliminar, text='Eliminar',width=15, justify="center", font=("", 12),
                            command=lambda:SQLConexion.MetodosSQL.EliminarSQL(cod_eliminar.get().strip(), CodigoMovimiento))
    btnEliminar.grid(row=6, column=1,  columnspan=1,padx=5, pady=5, sticky="we")

    btnCancelar = tk.Button(Ventana_Eliminar, text='Cancelar', width=15,justify="center", font=("", 12), command=Ventana_Eliminar.destroy)
    btnCancelar.grid(row=6, column=2,  columnspan=1,padx=5, pady=5, sticky="we")

    # ventana para Elimianar 1 usuario
# ---------------------------------------------------------------------------------------------------------------------------------#
VentanaLogin()
ventana.mainloop()
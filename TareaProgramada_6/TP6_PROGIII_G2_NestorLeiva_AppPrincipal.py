import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import TP6_PROGIII_G2_NestorLeiva_SQLConexion as Conn


class MiApp:
    
    def IngresoLoginSQL(self ):
        try:
            self.usuario = self.txtUsuario.get().strip()
            contrasena = self.txtContrasena.get().strip()
            #self.usuario = "nestorsa" # borrar esta linea
            #contrasena = 'N$tr0436*' # borrar esta linea
            if Conn.ConexionSQL.LoginSQL(self.usuario, contrasena):
                self.ventana.withdraw()
                self.VentanaCajeros()
                self.Limpiar(self.txtUsuario, self.txtContrasena)
            else:
                self.Limpiar(self.txtUsuario, self.txtContrasena)
                messagebox.showerror('Tarea Programada 6','Credenciales Incorrectas')

            self.metodos_sql.ObtenerUsuario(self.usuario) # obtengo el usuario 
        
        except ValueError as e:
            print(f'Credenciales Incorrectas {e}')           
    # fin IngresoLoginSQL

    def CerrarSesion(self,ventana):
        Conn.ConexionSQL.CerrarSQL() 
        ventana.withdraw() # oculta la ventana
        self.ventana.deiconify()  # muestra la ventana
        print('Se Realizo el cierr de la Sesion')
        print('ingreso al login')
    # Metodo para realizar el cierre de la sesion

    def RegresarVentanaCajeros(self):
        try:
            # cierra la ventana Cajero1
            if self.ventana_Cajero1 is not None:
                self.ventana_Cajero1.destroy()
                self.ventana_Cajero1 = None
                print('Cierre de la ventana cajero 1')
            else:
                print('No se cerro la ventana cajero 1')
            # cierra la ventana Cajero2
            if self.ventana_Cajero2 is not None:
                self.ventana_Cajero2.destroy()
                self.ventana_Cajero2 = None
                print('Cierre de la ventana cajero 2')
            else:
                print('No se cerro la ventana cajero 2')
            # cierra la ventana Cajero3
            if self.ventana_Cajero3 is not None:
                self.ventana_Cajero3.destroy()
                self.ventana_Cajero3 = None
                print('Cierre de la ventana cajero 3')
            else:
                print('No se cerro la ventana cajero 3')
            # cierra la ventana Opciones de Cajero
            if self.VentanaOpcionesCajeros is not None:
                self.VentanaOpcionesCajeros.destroy()
                self.VentanaOpcionesCajeros = None
                print('Cierre de la ventana Opciones Cajero')
            else:
                print('No se cerro la ventana Opciones Cajero')
            # cierra la Ventana_Cambio_Estado
            if self.Ventana_Cambio_Estado is not None:
                self.Ventana_Cambio_Estado.destroy()
                self.Ventana_Cambio_Estado = None
            else:
                print('No se cerro la ventana Cambio Estado Cajero')

            # cierra la VentanaDeposito
            if self.ventana_Deposito is not None:
                self.ventana_Deposito.destroy()
                self.ventana_Deposito = None
            else:
                print('No se cerro la Ventana Deposito')

            # cierra la VentanaRetiro
            if self.ventana_Retiros is not None:
                self.ventana_Retiros.destroy()
                self.ventana_Retiros = None
            else:
                print('No se cerro la Ventana Retiro')

            # cierra la VentanaConsulta
            if self.ventana_Consulta is not None:
                self.ventana_Consulta.destroy()
                self.ventana_Consulta = None
            else:
                print('No se cerro la Ventana Consulta')

            # se muestra la ventana si existe
            if self.ventana_Cajeros is not None: 
                self.ventana_Cajeros.deiconify()
               
            print('Regresando a la ventana anterior')
        except ValueError as e:
            print(f'Error{e}')
    # Metodo para Regresar a la ventana Anterior

    def Limpiar(self, *TextoWidget):
        for texto in TextoWidget:
            if isinstance(texto, (tk.Entry, tk.Text)):  
                texto.delete(0, "end")
    # Metodo para limpiar Texbox    
    #-----------------------------------------------------------------------------------------#
    def EstadoCajero(self,num_cajero):
        try:
            cajero = self.metodos_sql.ConsutaCajero(num_cajero)
            if num_cajero == 1:
                if cajero == 'L':
                    self.btnImg1.config(state='active')
                    self.btnCajero1.config(state='active')
                    self.btnIngresoCajero1.config(state='active')
                    print('Bontones Activos Cajero 1')
                    print('Cajero Libre')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero Libre')
                elif cajero == 'O':
                    self.btnImg1.config(state='disabled')
                    self.btnCajero1.config(state='disabled')
                    self.btnIngresoCajero1.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 1')
                    print('Cajero Ocupado')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero Ocupado')
                elif cajero == 'M':
                    self.btnImg1.config(state='disabled')
                    self.btnCajero1.config(state='disabled')
                    self.btnIngresoCajero1.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 1')
                    print('Cajero en Mantenimiento')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero En Mantenimiento')
                elif cajero == 'F':
                    self.btnImg1.config(state='disabled')
                    self.btnCajero1.config(state='disabled')
                    self.btnIngresoCajero1.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 1')
                    print('Cajero Fuera de Servicio')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero Fuera de Servicio')
            elif num_cajero == 2:
                if cajero == 'L':
                    self.btnImg2.config(state='active')
                    self.btnCajero2.config(state='active')
                    self.btnIngresoCajero2.config(state='active')
                    print('Bontones Activos Cajero 2')
                    print('Cajero Libre')
                elif cajero == 'O':
                    self.btnImg2.config(state='disabled')
                    self.btnCajero2.config(state='disabled')
                    self.btnIngresoCajero2.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 2')
                    print('Cajero Ocupado')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero Ocupado')
                elif cajero == 'M':
                    self.btnImg2.config(state='disabled')
                    self.btnCajero2.config(state='disabled')
                    self.btnIngresoCajero2.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 2')
                    print('Cajero en Mantenimiento')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero En Mantenimiento')
                elif cajero == 'F':
                    self.btnImg2.config(state='disabled')
                    self.btnCajero2.config(state='disabled')
                    self.btnIngresoCajero2.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 2')
                    print('Cajero Fuera de Servicio')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero Fuera de Servicio')
            elif num_cajero == 3:
                if cajero == 'L':
                    self.btnImg3.config(state='active')
                    self.btnCajero3.config(state='active')
                    self.btnIngresoCajero3.config(state='active')
                    print('Bontones Activos Cajero 3')
                    print('Cajero Libre')
                elif cajero == 'O':
                    self.btnImg3.config(state='disabled')
                    self.btnCajero3.config(state='disabled')
                    self.btnIngresoCajero3.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 3')
                    print('Cajero Ocupado')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero Ocupado')
                elif cajero == 'M':
                    self.btnImg3.config(state='disabled')
                    self.btnCajero3.config(state='disabled')
                    self.btnIngresoCajero3.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 3')
                    print('Cajero en Mantenimiento')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero En Mantenimiento')
                elif cajero == 'F':
                    self.btnImg3.config(state='disabled')
                    self.btnCajero3.config(state='disabled')
                    self.btnIngresoCajero3.config(state='disabled')
                    print('Boton Ingresar Desactivado Cajero 3')
                    print('Cajero Fuera de Servicio')
                    messagebox.showwarning('Tarea Programada 6', 'Cajero Fuera de Servicio')
            else:
                print(f'Error al seleccionar el numero de Cajero: _{num_cajero}_')
        except ValueError as e:
            print('Error al cambiar el Estado de las Ventanas : {e}')
    # Metodo para cambiar el estado de las ventanas
    #-----------------------------------------------------------------------------------------#
    def __init__(self, root):
        self.ventana = root
        self.ventana.title('Tarea Programad6 - a Cajero Automatico')
        self.ventana.geometry('500x200')
        print('ventana Login')
        #-----------------------------------------------------------------------------------------#
        self.metodos_sql = Conn.MetodosSQL()
        self.estado = None
        self.cajero = None
        self.ventana_Cajero1 = None
        self.ventana_Cajero2 = None
        self.ventana_Cajero3 = None
        self.VentanaOpcionesCajeros = None
        self.Ventana_Cambio_Estado = None
        self.ventana_Deposito = None
        self.ventana_Retiros = None
        self.ventana_Consulta = None
        
        self.btnImg1 = None
        self.btnImg2 = None
        self.btnCajero1 = None
        self.btnCajero2 = None
        self.btnIngresoCajero1 = None
        self.btnIngresoCajero2 = None
        #-----------------------------------------------------------------------------------------#

        lblTitulo = tk.Label(self.ventana, text="Ventana de Login", width=25,justify="center", bd=2, relief="solid", font=("", 12))
        lblTitulo.grid(row=1, column=1, columnspan=3,padx=10, pady=10, sticky="we")

        lblUsuario = tk.Label(self.ventana, text="Codigo de Usuario: ", width=20,justify="center", bd=2, relief="solid", font=("", 12))
        lblUsuario.grid(row=2, column=1, columnspan=1,padx=10, pady=10, sticky="we")

        self.txtUsuario = tk.Entry(self.ventana, width=20, justify="center", bd=2, relief="solid", font=("", 12))
        self.txtUsuario.grid(row=2, column=2, columnspan=2,padx=10, pady=10, sticky="we")
        self.txtUsuario.focus()

        lblContrasena = tk.Label(self.ventana, text="Contrasena / PIN: ", width=20, justify="center", bd=2, relief="solid", font=("", 12))
        lblContrasena.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="we")

        self.txtContrasena = tk.Entry(self.ventana, width=20, justify="center", bd=2, relief="solid", font=("", 12), show='*')
        self.txtContrasena.grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky="we")
        # ---------------------------------------------------------------#
        btnLogin = tk.Button(self.ventana, text="Login", width=10, justify="center", bd=2, relief="solid", font=("", 12), command= self.IngresoLoginSQL) 
        btnLogin.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky='we')

        btnLimpiar = tk.Button(self.ventana, text="Limpiar", width=10, justify="center", bd=2, relief="solid", font=("", 12))
        btnLimpiar.grid(row=4, column=2, columnspan=2, padx=10, pady=10, sticky='we')
    # Fin Metodo Constructor de la clase / Ventana de Login 
    
    def VentanaCajeros(self):
        try:
            self.ventana_Cajeros = tk.Toplevel(self.ventana)
            self.ventana_Cajeros.title('Tarea Programada 6 - Cajero Automatico')
            self.ventana_Cajeros.geometry('600x400')
            print('Ventana Cajeros')
            # ---------------------------------------------------------------#

            # ---------------------------------------------------------------#
            lblTitulo = tk.Label(self.ventana_Cajeros, text='Bienvenido al Banco Personal \n Cajero Digital', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
            lblTitulo.grid(row=1, column=1, columnspan=4, padx=10,pady=10, sticky='we')
            # ---------------------------------------------------------------#
            self.btnImg1 = tk.Button(self.ventana_Cajeros, text='img 1', command= self.VentanaCajero1)
            self.btnImg1.grid(row=2,column=2,columnspan=1, padx=10, pady=10)
            self.btnImg2 = tk.Button(self.ventana_Cajeros, text='img 2', command= self.VentanaCajero2)
            self.btnImg2.grid(row=2,column=3,columnspan=1, padx=10, pady=10)
            self.btnImg3 = tk.Button(self.ventana_Cajeros, text='img 3', command= self.VentanaCajero3)
            self.btnImg3.grid(row=2,column=4,columnspan=1, padx=10, pady=10)
            # ---------------------------------------------------------------#
            self.btnCajero1 = tk.Button(self.ventana_Cajeros,text='Cajero # 1', width=10, justify='center',bd=2,font=("", 16), command= self.VentanaCajero1)
            self.btnCajero1.grid(row=3,column=2,columnspan=1, padx=10, pady=10)
            self.btnCajero2 = tk.Button(self.ventana_Cajeros,text='Cajero # 2', width=10, justify='center',bd=2,font=("", 16), command= self.VentanaCajero2)
            self.btnCajero2.grid(row=3,column=3,columnspan=1, padx=10, pady=10)
            self.btnCajero3 = tk.Button(self.ventana_Cajeros,text='Cajero # 3', width=10, justify='center',bd=2,font=("", 16), command= self.VentanaCajero3)
            self.btnCajero3.grid(row=3,column=4,columnspan=1, padx=10, pady=10)
            # ---------------------------------------------------------------#
            btnTerminar = tk.Button(self.ventana_Cajeros, text="Salir del Cajero", width=10, justify="center", bd=2, relief="solid", font=("", 12), command=lambda: self.CerrarSesion(self.ventana_Cajeros))
            btnTerminar.grid(row=4, column=3, columnspan=1, padx=10, pady=10, sticky='we')
        except ValueError as e:
            print(f'Error al Cargar la Ventana de los Cajeros {e}')
  # Fin VentanaCajeros

    def VentanaCajero1(self,cajero =1):
        print('Cajero # 1')
        self.ventana_Cajeros.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Cajero1 = tk.Toplevel(self.ventana)
        self.ventana_Cajero1.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Cajero1.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Cajero1, text='Bienvenido al Banco Personal \n Cajero Digital # 1', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=3, padx=10,pady=10, sticky='we')

        self.btnIngresoCajero1 = tk.Button(self.ventana_Cajero1,text='Ingreso', width=10, justify='center',bd=2,font=("", 16), command= self.OpcionesCajero)
        self.btnIngresoCajero1.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

        self.EstadoCajero(cajero,) 

        btnRegresar = tk.Button(self.ventana_Cajero1,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10) 
    # Fin Ventana Cajero 1

    def VentanaCajero2(self,cajero =2):
        print('Cajero # 2')
        self.ventana_Cajeros.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Cajero2 = tk.Toplevel(self.ventana)
        self.ventana_Cajero2.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Cajero2.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Cajero2, text='Bienvenido al Banco Personal \n Cajero Digital # 2', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=3, padx=10,pady=10, sticky='we')

        self.btnIngresoCajero2 = tk.Button(self.ventana_Cajero2,text='Ingreso', width=10, justify='center',bd=2,font=("", 16), command= self.OpcionesCajero)
        self.btnIngresoCajero2.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

        self.EstadoCajero(cajero,) 
        
        btnRegresar = tk.Button(self.ventana_Cajero2,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
    # Fin Ventana Cajero 2

    def VentanaCajero3(self,cajero = 3):
        print('Cajero # 3')
        self.ventana_Cajeros.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Cajero3 = tk.Toplevel(self.ventana)
        self.ventana_Cajero3.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Cajero3.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Cajero3, text='Bienvenido al Banco Personal \n Cajero Digital # 3', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=3, padx=10,pady=10, sticky='we')

        self.btnIngresoCajero3 = tk.Button(self.ventana_Cajero3,text='Ingreso', width=10, justify='center',bd=2,font=("", 16), command= self.OpcionesCajero)
        self.btnIngresoCajero3.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

        self.EstadoCajero(cajero,) 
        
        btnRegresar = tk.Button(self.ventana_Cajero3,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
    # Fin Ventana Cajero 3

    def OpcionesCajero(self):
        if self.ventana_Cajero1: 
            self.ventana_Cajero1.withdraw()
        elif  self.ventana_Cajero2:
            self.ventana_Cajero2.withdraw()
        elif  self.ventana_Cajero3:
            self.ventana_Cajero3.withdraw()

        self.VentanaOpcionesCajeros = tk.Toplevel(self.ventana)
        self.VentanaOpcionesCajeros.title('Tarea Programada 6 - Cajero Automatico')
        self.VentanaOpcionesCajeros.geometry('600x400')
        print('Opciones Cajeros ')

        
        lblTitulo = tk.Label(self.VentanaOpcionesCajeros, text="Banco Personal \n Que Accion desea Realizar", width=25,justify="center", bd=2, relief="solid", font=("", 24))
        lblTitulo.grid(row=0, column=0, columnspan=3,padx=50, pady=10, sticky="we")

        btnRealizarDeposito = tk.Button(self.VentanaOpcionesCajeros, text="Deposito", width=20, justify='center',bd=2,font=("", 16), command= self.VentanaDeposito )
        btnRealizarDeposito.grid(row=1, column=0,columnspan=1 ,padx=10, pady=10)

        btnRealizarRetiro = tk.Button(self.VentanaOpcionesCajeros, text="Retiro", width=20, justify='center',bd=2,font=("", 16), command= self.VentanaRetiro )
        btnRealizarRetiro.grid(row=1, column=1,columnspan=1 ,padx=10, pady=10)

        btnRealizarConsulta = tk.Button(self.VentanaOpcionesCajeros, text="Consulta", width=20, justify='center',bd=2,font=("", 16), command= self.VentanaConsulta )
        btnRealizarConsulta.grid(row=2, column=0,columnspan=1 ,padx=10, pady=10)

        btnRealizarCambioEstado = tk.Button(self.VentanaOpcionesCajeros, text="Cambio de Estado ATM", width=20, justify='center',bd=2,font=("", 16), command= self.VentanaCambioEstado )
        btnRealizarCambioEstado.grid(row=2, column=1,columnspan=1 ,padx=10, pady=10)

        btnRegresar = tk.Button(self.VentanaOpcionesCajeros,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
    # Fin OpcionesCajero

    def VentanaCambioEstado(self):
        self.VentanaOpcionesCajeros.withdraw()
        # ---------------------------------------------------------------#
        print('ventana Cambio Estado')
        self.Ventana_Cambio_Estado = tk.Toplevel(self.ventana)
        self.Ventana_Cambio_Estado.title('Tarea Programada 6 - Cajero Automatico')
        self.Ventana_Cambio_Estado.geometry('600x400')
        print('Cambio De Estado Cajeros')


        lblTitulo = tk.Label(self.Ventana_Cambio_Estado, text="Banco Personal \n Que Accion desea Realizar", width=25,justify="center", bd=2, relief="solid", font=("", 24))
        lblTitulo.grid(row=0, column=0, columnspan=3,padx=50, pady=10, sticky="we")

        lblCambio = tk.Label(self.Ventana_Cambio_Estado, text="Seleccione el Cajero a Cambiar", width=25,justify="center", bd=2, relief="solid", font=("", 14))
        lblCambio.grid(row=1, column=0, columnspan=1,padx=10, pady=10, sticky="we")

        txtCambioCajero = tk.Entry(self.Ventana_Cambio_Estado, width=20, justify="center", bd=2, relief="solid", font=("", 12))
        txtCambioCajero.grid(row=1, column=1, columnspan=2,padx=10, pady=10, sticky="we")
        txtCambioCajero.focus()
        
        def ObtenerNuevoEstado(nuevoEstado):
            num_cajero = (txtCambioCajero.get())
            self.metodos_sql.MovimientoCajero(num_cajero, nuevoEstado)
            self.Limpiar(txtCambioCajero)
        

        btnEstadoLibre = tk.Button(self.Ventana_Cambio_Estado,text='Libre', width=20, justify='center',bd=2,font=("", 16), command=lambda:ObtenerNuevoEstado('L'))
        btnEstadoLibre.grid(row=3, column=0, columnspan=1, padx=10, pady=10)

        btnEstadoOcupado = tk.Button(self.Ventana_Cambio_Estado,text='Ocupado', width=20, justify='center',bd=2,font=("", 16), command=lambda:ObtenerNuevoEstado('O'))
        btnEstadoOcupado.grid(row=3, column=1, columnspan=1, padx=10, pady=10)

        btnEstadoMantenimiento = tk.Button(self.Ventana_Cambio_Estado,text='Mantinimiento', width=20, justify='center',bd=2,font=("", 16), command=lambda:ObtenerNuevoEstado('M'))
        btnEstadoMantenimiento.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

        btnEstadoFueraServicio = tk.Button(self.Ventana_Cambio_Estado,text='Fuera Servicio', width=20, justify='center',bd=2,font=("", 16), command=lambda:ObtenerNuevoEstado('F'))
        btnEstadoFueraServicio.grid(row=4, column=1, columnspan=1, padx=10, pady=10)

        btnRegresar = tk.Button(self.Ventana_Cambio_Estado,text='Regresar', width=20, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)  
    # Fin VentanCambioEstado
    #-----------------------------------------------------------------------------------------#
    def VentanaDeposito(self):
        print('Ventana Deposito')
        self.VentanaOpcionesCajeros.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Deposito = tk.Toplevel(self.ventana)
        self.ventana_Deposito.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Deposito.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Deposito, text='Bienvenido al Banco Personal \n Depostitos', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=10,pady=10, sticky='we')

        lblIngresoSaldo = tk.Label(self.ventana_Deposito, text='Ingrese Monto de Deposito', width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        lblIngresoSaldo.grid(row=1, column=0, columnspan=1, padx=10,pady=10, sticky='we')

        txtIngresoSaldo = tk.Entry(self.ventana_Deposito, width=20, justify="center", bd=2, relief="solid", font=("", 14))
        txtIngresoSaldo.grid(row=1, column=1, columnspan=1,padx=10, pady=10, sticky="we")
        # ---------------------------------------------------------------#
            # se lanza el evento realizarDeposito 
        def OperacionDeposito():
            self.metodos_sql.RealizarDeposito (int(txtIngresoSaldo.get() ))
            self.Limpiar(txtIngresoSaldo)
        btnDepositarD = tk.Button(self.ventana_Deposito,text='Depositar', width=20, justify="center", bd=2,relief="solid", font=("", 14),
                        command= OperacionDeposito   )
        btnDepositarD.grid(row=2, column=0, columnspan=2,padx=10, pady=10, sticky="we")    
        # ---------------------------------------------------------------#
        lblSaldoActual = tk.Label(self.ventana_Deposito, text='Saldo Anterior', width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        lblSaldoActual.grid(row=3, column=0, columnspan=1, padx=10,pady=10, sticky='we')
        lblSaldoActual.config(state='disabled')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#
            # muestro el saldo anterior
        txtSaldoActual = tk.Entry(self.ventana_Deposito, width=20, justify="center", bd=2, relief="solid", font=("", 14))
        txtSaldoActual.grid(row=3, column=1, columnspan=1,padx=10, pady=10, sticky="we")
        saldoAnte = self.metodos_sql.ConsultaSaldo()
        txtSaldoActual.delete(0,tk.END)
        txtSaldoActual.insert(0, saldoAnte)
        txtSaldoActual.config(state='disabled')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#

        lblMontoDeposito = tk.Label(self.ventana_Deposito, text='Saldo Actual', width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        lblMontoDeposito.grid(row=4, column=0, columnspan=1, padx=10,pady=10, sticky='we')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#
        txtMontoDeposito = tk.Entry(self.ventana_Deposito, width=20, justify="center", bd=2, relief="solid", font=("", 14))
        txtMontoDeposito.grid(row=4, column=1, columnspan=1,padx=10, pady=10, sticky="we")

        txtMontoDeposito.config(state='disabled')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#
        self.btnCancelarD = tk.Button(self.ventana_Deposito,text='Cancelar', width=20, justify="center", bd=2, relief="solid", font=("", 14))
        self.btnCancelarD.grid(row=5, column=0, columnspan=1,padx=10, pady=10, sticky="we")

        self.btnRegresarD = tk.Button(self.ventana_Deposito,text='Regresar', width=20, justify="center", bd=2, relief="solid", font=("", 14), command= self.RegresarVentanaCajeros )
        self.btnRegresarD.grid(row=5, column=1, columnspan=1,padx=10, pady=10, sticky="we")
    # Metodo para Realizar Depositos

    def VentanaRetiro(self):
        print('Ventana Retiros')
        self.VentanaOpcionesCajeros.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Retiros = tk.Toplevel(self.ventana)
        self.ventana_Retiros.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Retiros.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Retiros, text='Bienvenido al Banco Personal \n Retiiros', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=10,pady=10, sticky='we')
        # ---------------------------------------------------------------#
        lblIngresoSaldo = tk.Label(self.ventana_Retiros, text='Saldo Anterior', width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        lblIngresoSaldo.grid(row=2, column=0, columnspan=1, padx=10,pady=10, sticky='we')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#
        self.txtSaldoAnterior = tk.Entry(self.ventana_Retiros, width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        self.txtSaldoAnterior.grid(row=2, column=1, columnspan=1, padx=10,pady=10, sticky='we')
        saldoAnt = self.metodos_sql.ConsultaSaldo()
        self.txtSaldoAnterior.delete(0,tk.END)
        self.txtSaldoAnterior.insert(0,saldoAnt) 
        self.txtSaldoAnterior.config(state='disabled')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#
        lblIngresoSaldo = tk.Label(self.ventana_Retiros, text='Ingrese Monto de Retiro', width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        lblIngresoSaldo.grid(row=3, column=0, columnspan=1, padx=10,pady=10, sticky='we')

        txtRetiroSaldo = tk.Entry(self.ventana_Retiros, width=20, justify="center", bd=2, relief="solid", font=("", 14))
        txtRetiroSaldo.grid(row=3, column=1, columnspan=1,padx=10, pady=10, sticky="we")
        txtRetiroSaldo.focus()
        # ---------------------------------------------------------------#
        def OperacionRetiro():
            self.metodos_sql.RealizarRetiro (int(txtRetiroSaldo.get()))
            self.Limpiar(txtRetiroSaldo)

        btnRetiroR = tk.Button(self.ventana_Retiros,text='Retiro', width=20, justify="center", bd=2, relief="solid", font=("", 14),command= OperacionRetiro ) 
        btnRetiroR  .grid(row=4, column=0, columnspan=1,padx=10, pady=10, sticky="we")
        # ---------------------------------------------------------------#
        btnCancelarR = tk.Button(self.ventana_Retiros,text='Cancelar', width=20, justify="center", bd=2, relief="solid", font=("", 14))
        btnCancelarR.grid(row=4, column=1, columnspan=1,padx=10, pady=10, sticky="we")

        btnRegresarR = tk.Button(self.ventana_Retiros,text='Regresar', width=20, justify="center", bd=2, relief="solid", font=("", 14), command= self.RegresarVentanaCajeros )
        btnRegresarR.grid(row=5, column=0, columnspan=1,padx=10, pady=10, sticky="we")
    # Fin VentanaRetiro

    def VentanaConsulta(self):
        print('Ventana Consulta')
        self.VentanaOpcionesCajeros.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Consulta = tk.Toplevel(self.ventana)
        self.ventana_Consulta.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Consulta.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Consulta, text='Bienvenido al Banco Personal \n Consulta', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=2, padx=10,pady=10, sticky='we')
        # ---------------------------------------------------------------#
        lblSaldoC = tk.Label(self.ventana_Consulta, text='Saldo Actual', width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        lblSaldoC.grid(row=2, column=0, columnspan=1, padx=10,pady=10, sticky='we')

        self.txtSaldoC = tk.Entry(self.ventana_Consulta, width=15 , justify='center', bd=2,relief="solid",font=("", 14) )
        self.txtSaldoC.grid(row=2, column=1, columnspan=1, padx=10,pady=10, sticky='we')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#
        saldo = self.metodos_sql.ConsultaSaldo() 
        # realizo la consulta a base datos
        self.txtSaldoC.delete(0,tk.END) # elimino el dato almacenado anterios
        self.txtSaldoC.insert(0,saldo) # Inserto el saldo al txt
        self.txtSaldoC.config(state='disabled')
        # ---------------------------------------------------------------#
        # ---------------------------------------------------------------#
        self.btnRegresarR = tk.Button(self.ventana_Consulta,text='Regresar', width=20, justify="center", bd=2, relief="solid", font=("", 14), command= self.RegresarVentanaCajeros )
        self.btnRegresarR.grid(row=3, column=1, columnspan=1,padx=10, pady=10, sticky="we")
    # Fin VentanaConsulta

# Fin de class MiApp
#-----------------------------------------------------------------------------------------#
root = tk.Tk() # se crea la ventana#
app = MiApp(root) # se inicializa la aplicacion
root.mainloop() # se inicializa el bucle principal
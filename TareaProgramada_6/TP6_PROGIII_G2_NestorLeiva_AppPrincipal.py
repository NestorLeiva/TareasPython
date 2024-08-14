import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import TP6_PROGIII_G2_NestorLeiva_SQLConexion as Conn

class MiApp:
    rutaRelativaPng = (r'..\img\cajero-automatico.png')
    rutaRelativaIco = (r'..\img\cajero-automatico.ico') # .. indica subir un nivelen la ruta
     
    def IngresoLoginSQL(self ):
        try:
            #usuario = self.txtUsuario.get().strip()
            #contrasena = self.txtContrasena.get().strip()
            usuario = "NestorC" # borrar esta linea
            contrasena = 'nestor10' # borrar esta linea
            if Conn.ConexionSQL.LoginSQL(usuario, contrasena):
                self.ventana.withdraw()
                self.VentanaCajeros()
                self.Limpiar(self.txtUsuario, self.txtContrasena)
            else:
                self.Limpiar(self.txtUsuario, self.txtContrasena)
                messagebox.showerror('Tarea Programada 6','Credenciales Incorrectas')
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
        
    def RegresarVentana(self, ventana):
        ventana.withdraw() # oculta la ventana
        self.ventana.deiconify()  # muestra la ventana
        print('Se regreso a la ventana anterior')
    # Metodo para regresar a la ventana anterior

    def RegresarVentanaCajeros(self):
        # cierra la ventana Cajero1
        if self.ventana_Cajero1 is not None:
            self.ventana_Cajero1.destroy()
            self.ventana_Cajero1 = None

        # cierra la ventana Opciones de Cajero
        if self.VentanaOpcionesCajeros is not None:
            self.VentanaOpcionesCajeros.destroy()
            self.VentanaOpcionesCajeros = None


        # se muestra la ventana si existe
        if self.ventana_Opciones is not None: 
            self.ventana_Opciones.deiconify()
        print('Regresando a la ventana anterior')

    def Limpiar(self, *TextoWidget):
        for texto in TextoWidget:
            if isinstance(texto, (tk.Entry, tk.Text)):  
                texto.delete(0, "end")
    # Metodo para limpiar Texbox    
    #-----------------------------------------------------------------------------------------#

    def TipoEstadoCajero(self,estado):
        if estado == 2: 
            print('Cajero Ocupado')
            messagebox.showwarning('Tarea Programada 6', 'Cajero Ocupado')
        elif  estado == 3:
            print('Cajero En Mantinimiento')
            messagebox.showwarning('Tarea Programada 6', 'Cajero En Mantenimiento')
        elif estado == 4:
            print('Cajero de Fuera Servicio')
            messagebox.showwarning('Tarea Programada 6', 'Cajero Fuera de Servicio')
    # Metodo Tipo Estado Del Cajero

    def EstadoCajero(self,cajero=None, estado=None):

        if cajero == 1: #Cajero # 1

            if (estado == 2 or estado == 3 or estado == 4): 
                    self.btnImg1.config(state='disabled')
                    self.btnCajero1.config(state='disabled')
                    self.btnIngresoCajero1.config(state='disabled')
                    self.TipoEstadoCajero(estado)                  
                    print('Boton Desactivado Cajero 1')
                    #-----------------------------------------------------------------------------------------#
            elif estado == 1 :
                    self.btnImg1.config(state='active')
                    self.btnCajero1.config(state='active')
                    self.btnIngresoCajero1.config(state='active')
                    print('Bontones Activos Cajero 1')
                    #-----------------------------------------------------------------------------------------#
            else:
                print('Error al Desactivar los bontones')

        elif cajero == 2: # Cajero # 2

            if (estado == 2 or estado == 3 or estado == 4): 
                    print('Boton Desactivado Cajero 2')
                    #-----------------------------------------------------------------------------------------#
                    self.btnImg2.config(state='disabled')
                    self.btnCajero2.config(state='disabled')
                    self.btnIngresoCajero2.config(state='disabled')
                    self.TipoEstadoCajero(estado)
                    print('Boton Desactivado Cajero 2')
            elif estado == 1 :
                    print('Bontones Activos Cajero 2')
                    #-----------------------------------------------------------------------------------------#
                    self.btnImg2.config(state='active')
                    self.btnCajero2.config(state='active')
                    self.btnIngresoCajero2.config(state='active')
            else:
                print('Error al Desactivar los bontones')

        elif cajero == 3: # Cajero # 3

            if (estado == 2 or estado == 3 or estado == 4): 
                    print('Boton Desactivado Cajero 2')
                    #-----------------------------------------------------------------------------------------#
                    self.btnImg3.config(state='disabled')
                    self.btnCajero3.config(state='disabled')
                    self.btnIngresoCajero3.config(state='disabled')
                    self.TipoEstadoCajero(estado)
                    print('Boton Desactivado Cajero 3')
            elif estado == 1 :
                    print('Bontones Activos Cajero 2')
                    #-----------------------------------------------------------------------------------------#
                    self.btnImg3.config(state='active')
                    self.btnCajero3.config(state='active')
                    self.btnIngresoCajero3.config(state='active')
            else:
                print('Error al Desactivar los bontones')
        else:
             print('Error con los Cajeros')

    # Metodo para realiza la validacion del estado del cajero 
    #-----------------------------------------------------------------------------------------#
    def __init__(self, root):
        self.ventana = root
        self.ventana.title('Tarea Programad6 - a Cajero Automatico')
        self.ventana.geometry('500x200')
        self.ventana.iconbitmap(MiApp.rutaRelativaIco) # agregar icono 
        print('ventana Login')
        #-----------------------------------------------------------------------------------------#
        self.cajero = None
        self.ventana_Cajero1 = None
        self.ventana_Cajero2 = None
        self.ventana_Opciones = None
        self.VentanaOpcionesCajeros = None
        
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
        self.ventana_Opciones = tk.Toplevel(self.ventana)
        self.ventana_Opciones.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Opciones.geometry('600x400')
        print('Ventana Cajeros')
        # ---------------------------------------------------------------#
        self.ventana.iconbitmap(MiApp.rutaRelativaIco) # agregar icono 
        self.imagen = tk.PhotoImage(file= MiApp.rutaRelativaPng) # se carga la imagen
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Opciones, text='Bienvenido al Banco Personal \n Cajero Digital', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=1, column=1, columnspan=4, padx=10,pady=10, sticky='we')
        # ---------------------------------------------------------------#
        self.btnImg1 = tk.Button(self.ventana_Opciones, image=self.imagen, command= self.VentanaCajero1)
        self.btnImg1.grid(row=2,column=2,columnspan=1, padx=10, pady=10)
        self.btnImg2 = tk.Button(self.ventana_Opciones, image=self.imagen, command= self.VentanaCajero2)
        self.btnImg2.grid(row=2,column=3,columnspan=1, padx=10, pady=10)
        self.btnImg3 = tk.Button(self.ventana_Opciones, image=self.imagen, command= self.VentanaCajero3)
        self.btnImg3.grid(row=2,column=4,columnspan=1, padx=10, pady=10)
        # ---------------------------------------------------------------#
        self.btnCajero1 = tk.Button(self.ventana_Opciones,text='Cajero # 1', width=10, justify='center',bd=2,font=("", 16), command= self.VentanaCajero1)
        self.btnCajero1.grid(row=3,column=2,columnspan=1, padx=10, pady=10)
        self.btnCajero2 = tk.Button(self.ventana_Opciones,text='Cajero # 2', width=10, justify='center',bd=2,font=("", 16), command= self.VentanaCajero2)
        self.btnCajero2.grid(row=3,column=3,columnspan=1, padx=10, pady=10)
        self.btnCajero3 = tk.Button(self.ventana_Opciones,text='Cajero # 3', width=10, justify='center',bd=2,font=("", 16), command= self.VentanaCajero3)
        self.btnCajero3.grid(row=3,column=4,columnspan=1, padx=10, pady=10)
        # ---------------------------------------------------------------#
        btnTerminar = tk.Button(self.ventana_Opciones, text="Salir del Cajero", width=10, justify="center", bd=2, relief="solid", font=("", 12), command=lambda: self.CerrarSesion(self.ventana_Opciones))
        btnTerminar.grid(row=4, column=3, columnspan=1, padx=10, pady=10, sticky='we')
    # Fin VentanaCajeros

    def VentanaCajero1(self,cajero =1, estado=1):
        print('Cajero # 1')
        print(f'Estado del cajero {estado}')
        self.ventana_Opciones.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Cajero1 = tk.Toplevel(self.ventana)
        self.ventana_Cajero1.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Cajero1.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Cajero1, text='Bienvenido al Banco Personal \n Cajero Digital # 1', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=3, padx=10,pady=10, sticky='we')

        self.btnIngresoCajero1 = tk.Button(self.ventana_Cajero1,text='Ingreso', width=10, justify='center',bd=2,font=("", 16), command= self.OpcionesCajero)
        self.btnIngresoCajero1.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

        self.EstadoCajero(cajero,estado) 

        btnRegresar = tk.Button(self.ventana_Cajero1,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
    # Fin Ventana Cajero 1

    def VentanaCajero2(self,cajero =2, estado=2):
        print('Cajero # 2')
        
        self.ventana_Opciones.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Cajero2 = tk.Toplevel(self.ventana)
        self.ventana_Cajero2.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Cajero2.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Cajero2, text='Bienvenido al Banco Personal \n Cajero Digital # 2', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=3, padx=10,pady=10, sticky='we')

        self.btnIngresoCajero2 = tk.Button(self.ventana_Cajero2,text='Ingreso', width=10, justify='center',bd=2,font=("", 16), command= self.OpcionesCajero)
        self.btnIngresoCajero2.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

        self.EstadoCajero(cajero,estado) 
        
        btnRegresar = tk.Button(self.ventana_Cajero2,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
        
    # Fin Ventana Cajero 2

    def VentanaCajero3(self,cajero = 3, estado=3):
        
        print('Cajero # 3')
        
        self.ventana_Opciones.withdraw() # oculto la ventana
        # ---------------------------------------------------------------#
        self.ventana_Cajero3 = tk.Toplevel(self.ventana)
        self.ventana_Cajero3.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana_Cajero3.geometry('600x400')
        # ---------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana_Cajero3, text='Bienvenido al Banco Personal \n Cajero Digital # 2', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=0, column=0, columnspan=3, padx=10,pady=10, sticky='we')

        self.btnIngresoCajero3 = tk.Button(self.ventana_Cajero3,text='Ingreso', width=10, justify='center',bd=2,font=("", 16), command= self.OpcionesCajero)
        self.btnIngresoCajero3.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

        self.EstadoCajero(cajero,estado) 
        
        btnRegresar = tk.Button(self.ventana_Cajero3,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
        
    # Fin Ventana Cajero 2

    def OpcionesCajero(self):
        self.VentanaOpcionesCajeros = tk.Toplevel(self.ventana)
        self.VentanaOpcionesCajeros.title('Tarea Programada 6 - Cajero Automatico')
        self.VentanaOpcionesCajeros.geometry('600x400')
        print('Opciones Cajero')
        #self.ventana_Cajero1.withdraw()
        #self.ventana_Cajero2.withdraw()
        
        lblTitulo = tk.Label(self.VentanaOpcionesCajeros, text="Banco Personal \n Que Accion desea Realizar", width=25,justify="center", bd=2, relief="solid", font=("", 24))
        lblTitulo.grid(row=0, column=0, columnspan=3,padx=50, pady=10, sticky="we")

        btnRealizarDeposito = tk.Button(self.VentanaOpcionesCajeros, text="Deposito", width=20, justify='center',bd=2,font=("", 16), command= self.VentanaDeposito )
        btnRealizarDeposito.grid(row=1, column=0,columnspan=1 ,padx=10, pady=10)

        btnRealizarRetiro = tk.Button(self.VentanaOpcionesCajeros, text="Retiro", width=20, justify='center',bd=2,font=("", 16), command= self.VentanaRetiro )
        btnRealizarRetiro.grid(row=1, column=1,columnspan=1 ,padx=10, pady=10)

        btnRealizarConsulta = tk.Button(self.VentanaOpcionesCajeros, text="Consulta", width=20, justify='center',bd=2,font=("", 16), command= self.VentanaConsulta )
        btnRealizarConsulta.grid(row=2, column=0,columnspan=1 ,padx=10, pady=10)

        btnRealizarCambioEstado = tk.Button(self.VentanaOpcionesCajeros, text="Cambio de Estado ATM", width=20, justify='center',bd=2,font=("", 16) )
        btnRealizarCambioEstado.grid(row=2, column=1,columnspan=1 ,padx=10, pady=10)

        btnRegresar = tk.Button(self.VentanaOpcionesCajeros,text='Regresar', width=10, justify='center',bd=2,font=("", 16), command= self.RegresarVentanaCajeros )
        btnRegresar.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
    # Fin OpcionesCajero

    def VentanaCambioEstado(self, estado = None):
        messagebox.showinfo('Tarea Programad6 - a Cajero Automatico ', 'Opcion Cambio Estado Cajero')
        print('Opcion Cambio Estado Cajero')
        estado = None
        if estado == 1:
            self.EstadoLibre(self)
        elif estado == 2:
            self.EstadoOcupado(self)
        elif estado == 3:
            self.EstadoMantenimiento(self)
        elif estado == 4:
            self.EstadoFueraServicio(self)
        else: 
            print(' Error al cambiar estado Cajero')
        return estado
    # Fin VentanCambioEstado
    #-----------------------------------------------------------------------------------------#
    def VentanaDeposito(self):
        messagebox.showinfo('Tarea Programad6 - a Cajero Automatico ', 'Opcion Deposito')
        print('Opcion Deposito')
    # Fin VentanaDepositos

    def VentanaRetiro(self):
        messagebox.showinfo('Tarea Programad6 - a Cajero Automatico ', 'Opcion Retiro')
        print('Opcion Retiro')
    # Fin VentanaRetiro

    def VentanaConsulta(self):
        messagebox.showinfo('Tarea Programad6 - a Cajero Automatico ', 'Opcion Consulta Saldo')
        print('Opcion ConsultaSaldo')
    # Fin VentanaConsulta
    #-----------------------------------------------------------------------------------------#
    def EstadoLibre(self, estado = 1):
        print('Estado Libre')
        return estado
    #Fin EstadoLibre

    def EstadoOcupado(self, estado = 2):
        messagebox.showinfo('Tarea Programad6 - a Cajero Automatico ', 'Opcion Cambio Estado Cajero \n Ocupado')
        print('Estado Ocupado')
        return estado
    #Fin Estado Ocupado

    def EstadoMantenimiento(self, estado = 3):
        messagebox.showinfo('Tarea Programad6 - a Cajero Automatico ', 'Opcion Cambio Estado Cajero \n En Mantenimiento')
        print('Estado Mantenimiento')
        return  estado
    # Fin Estado Mantenimiento

    def EstadoFueraServicio(self, estado = 4):
        messagebox.showinfo('Tarea Programad6 - a Cajero Automatico ', 'Opcion Cambio Estado Cajero \n Fuera de Servicio')
        print('Estado Fuera Servicio')
        return estado
    # Fin Estado FueraServicio

# Fin de class MiApp
#-----------------------------------------------------------------------------------------#
root = tk.Tk() # se crea la ventana#

app = MiApp(root) # se inicializa la aplicacion
root.mainloop() # se inicializa el bucle principal
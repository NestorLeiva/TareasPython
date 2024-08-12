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
                messagebox.showerror(f'Credenciales Incorrectas: {usuario}')
        except ValueError as e:
            print(f'Credenciales Incorrectas {e}')           
    # fin IngresoLoginSQL

    def Limpiar(self, *TextoWidget):
        for texto in TextoWidget:
            if isinstance(texto, (tk.Entry, tk.Text)):  
                texto.delete(0, "end")
    # Metodo para limpiar Texbox

    def __init__(self, root):
        self.ventana = root
        self.ventana.title('Tarea Programada 6 - Cajero Automatico')
        self.ventana.geometry('500x200')
        self.ventana.iconbitmap(MiApp.rutaRelativaIco) # agregar icono 

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
        btnLimpiar.grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky='we')

        btnTerminar = tk.Button(self.ventana, text="Terminar", width=10, justify="center", bd=2, relief="solid", font=("", 12),  command=self.ventana.quit)
        btnTerminar.grid(row=4, column=3, columnspan=1, padx=10, pady=10, sticky='we')
    # Fin Metodo Constructor de la clase
    
    def VentanaCajeros(self):
        ventana_Opciones = tk.Toplevel(self.ventana)
        ventana_Opciones.title('Tarea Programada 6 - Cajero Automatico')
        ventana_Opciones.geometry('600x400')
        self.ventana.iconbitmap(MiApp.rutaRelativaIco) # agregar icono 
        self.imagen = tk.PhotoImage(file= MiApp.rutaRelativaPng) # se carga la imagen
        lblTitulo = tk.Label(ventana_Opciones, text='Bienvenido al Banco Personal \n Cajero Digital', width=30 , justify='center', bd=4,relief="solid",font=("", 24) )
        lblTitulo.grid(row=1, column=1, columnspan=4, padx=10,pady=10, sticky='we')
        # ---------------------------------------------------------------#
        btnImg1 = tk.Button(ventana_Opciones, image=self.imagen)
        btnImg1.grid(row=2,column=2,columnspan=1, padx=10, pady=10)
        btnImg2 = tk.Button(ventana_Opciones, image=self.imagen)
        btnImg2.grid(row=2,column=3,columnspan=1, padx=10, pady=10)
        btnImg3 = tk.Button(ventana_Opciones, image=self.imagen)
        btnImg3.grid(row=2,column=4,columnspan=1, padx=10, pady=10)
        # ---------------------------------------------------------------#
        btnCajero1 = tk.Button(ventana_Opciones,text='Cajero # 1', width=10, justify='center',bd=2,font=("", 16) )
        btnCajero1.grid(row=3,column=2,columnspan=1, padx=10, pady=10)
        btnCajero2 = tk.Button(ventana_Opciones,text='Cajero # 2', width=10, justify='center',bd=2,font=("", 16) )
        btnCajero2.grid(row=3,column=3,columnspan=1, padx=10, pady=10)
        btnCajero3 = tk.Button(ventana_Opciones,text='Cajero # 3', width=10, justify='center',bd=2,font=("", 16) )
        btnCajero3.grid(row=3,column=4,columnspan=1, padx=10, pady=10)
        # ---------------------------------------------------------------#
        btnTerminar = tk.Button(ventana_Opciones, text="Salir del Cajero", width=10, justify="center", bd=2, relief="solid", font=("", 12), command=ventana_Opciones.quit)
        btnTerminar.grid(row=4, column=3, columnspan=1, padx=10, pady=10, sticky='we')
    # Fin VentanaCajeros

    def OpcionesCajero(self):
        pass
    # Fin OpcionesCajero

    def VentanaDeposito(self):
        pass
    # Fin VentanaDepositos

    def VentanaRetiro(self):
        pass
    # Fin VentanaRetiro

    def VentanaConsulta(self):
        pass
    # Fin VentanaConsulta

    def VentanaCambioEstado(self):
        pass
    # Fin VentanCambioEstado
    def EstadoLibre(self):
        pass
    #Fin EstadoLibre

    def EstadoOcupado(self):
        pass
    #Fin Estado Ocupado

    def EstadoMantenimiento(self):
        pass
    # Fin Estado Mantenimiento

    def EstadoFueraServicio(self):
        pass
    # Fin Estado FueraServicio

# Fin de class MiApp
#-----------------------------------------------------------------------------------------#
root = tk.Tk() # se crea la ventana#
app = MiApp(root) # se inicializa la aplicacion
root.mainloop() # se inicializa el bucle principal
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import TP6_PROGIII_G2_NestorLeiva_SQLConexion 



class MiApp:

    def __init__(self, root):
        self.ventana = root
        self.ventana.title('Tarea Programada 5')
        self.ventana.geometry('500x200')
        
        #-----------------------------------------------------------------------------------------#
        #               Ventana Ingreso a los Cajeros
        #-----------------------------------------------------------------------------------------#
        lblTitulo = tk.Label(self.ventana, text="Ventana de Login", width=25,justify="center", bd=2, relief="solid", font=("", 12))
        lblTitulo.grid(row=1, column=1, columnspan=3,padx=10, pady=10, sticky="we")

        lblUsuario = tk.Label(self.ventana, text="Codigo de Usuario: ", width=20,justify="center", bd=2, relief="solid", font=("", 12))
        lblUsuario.grid(row=2, column=1, columnspan=1,padx=10, pady=10, sticky="we")

        txtUsuario = tk.Entry(self.ventana,  width=20, justify="center", bd=2, relief="solid", font=("", 12))
        txtUsuario.grid(row=2, column=2, columnspan=2,padx=10, pady=10, sticky="we")
        txtUsuario.focus()

        lblContrasena = tk.Label(self.ventana, text="Contrasena / PIN: ", width=20, justify="center", bd=2, relief="solid", font=("", 12))
        lblContrasena.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="we")

        txtContrasena = tk.Entry(self.ventana,  width=20, justify="center", bd=2, relief="solid", font=("", 12), show='*')
        txtContrasena.grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky="we")
        # ---------------------------------------------------------------#
        btnLogin = tk.Button(self.ventana, text="Login", width=10, justify="center", bd=2, relief="solid", font=("", 12) )
        btnLogin.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky='we')

        btnLimpiar = tk.Button(self.ventana, text="Limpiar", width=10, justify="center", bd=2, relief="solid", font=("", 12))
        btnLimpiar.grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky='we')

        btnTerminar = tk.Button(self.ventana, text="Terminar", width=10, justify="center", bd=2, relief="solid", font=("", 12),  command=self.ventana.quit)
        btnTerminar.grid(row=4, column=3, columnspan=1, padx=10, pady=10, sticky='we')
    # Fin Metodo Constructor de la clase
    
    def IngresoLoginSQL(self, usuario, contrasena):
        
            pass
    # fin IngresoLoginSQL


    def VentanaOpciones(self):
        rutaRelativaPng = (r'..\img\cajero-automatico.png')
        rutaRelativaIco = (r'..\img\cajero-automatico.ico') # .. indica subir un nivelen la ruta
        self.ventana.iconbitmap(rutaRelativaIco) # agregar icono 

        self.imagen = tk.PhotoImage(file= rutaRelativaPng) # se carga la imagen

        btnImg1 = tk.Button(self.ventana, image=self.imagen)
        btnImg1.grid(row=2,column=2,columnspan=1, padx=10, pady=10)
        btnImg2 = tk.Button(self.ventana, image=self.imagen)
        btnImg2.grid(row=2,column=3,columnspan=1, padx=10, pady=10)
        btnImg3 = tk.Button(self.ventana, image=self.imagen)
        btnImg3.grid(row=2,column=4,columnspan=1, padx=10, pady=10)
        pass
    # Fin VentanaOpciones

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
import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os


class MiApp:

    def __init__(self, root):
        self.ventana = root
        self.ventana.title('Tarea Programada 6, "Cajero Automatico"')
        self.ventana.geometry('500x500')
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



    # Metodo Constructor de la clase
    
    def VentanaOpciones(self):
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
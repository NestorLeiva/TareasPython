import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MiApp:

    def __init__(self, root):
        self.ventana = root
        self.ventana.title('Tarea Programada 6, "Cajero Automatico"')
        self.ventana.geometry('500x500')

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
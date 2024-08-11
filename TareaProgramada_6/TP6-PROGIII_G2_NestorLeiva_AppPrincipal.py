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
    
# Fin de class MiApp
#-----------------------------------------------------------------------------------------#
root = tk.Tk() # se crea la ventana
app = MiApp(root) # se inicializa la aplicacion
root.mainloop() # se inicializa el bucle principal
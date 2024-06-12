import tkinter as tk
#importacion de la clase Tkinter
""" -------------------------- Funciones -------------------------- """
def labelTitulo(ventana):
    label = tk.Label(text="Entrada de Numeros a Evaluar", font=("",15))
    label.pack(pady=50)
    # se realiza el empaquetado y se le anade el padding


""" -------------------------- Funcion Main -------------------------- """
ventana = tk.Tk() 
# objeto tipo ventana de la clase Tkinter
ventana.title("Primera Tarea Programada") 
# Titulo de la ventana
ventana.geometry("700x600")
# tamano de la ventana

labelTitulo(ventana)
ventana.mainloop()







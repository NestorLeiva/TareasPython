import tkinter as tk
#importacion de la clase Tkinter
""" -------------------------- Funciones -------------------------- """
def labelTitulo(ventana, x , y):
    label = tk.Label(ventana, text="Entrada de Numeros a Evaluar", font=("",15))
    label.place(x=x, y=y)
    # se realiza el posisionamiento del label por medio de las coordenadas
#Fin label_Titulo

def labelNumeros(ventana, x,y):
    label = tk.Label(ventana,text="Ingrese los 3 numeros a Evaluar", font=("",12))
    label.place(x=x, y=y)
#Fin label_Numeros

def labelNumeroMayor(ventana, x,y):
    label = tk.Label(ventana, text="Numero Mayor", font=("",12))
    label.place(x=x,y=y)
#Fin label_NumerosMayor

def labelNumeroMenor(ventana, x,y):
    label = tk.Label(ventana, text="Numero Menor", font=("",12))
    label.place(x=x,y=y)
#Fin label_NumerosMenor

def labelNumeroMayorMultiplicado(ventana, x,y):
    label = tk.Label(ventana, text="Numero Mayor multiplicado & en Potencia", font=("",12))
    label.place(x=x,y=y)
#Fin label_NumerosMayor&Potencia

def labelNumeroMenorMultiplicado(ventana, x,y):
    label = tk.Label(ventana, text="Numero Menor multiplicado & en Potencia", font=("",12))
    label.place(x=x,y=y)
#Fin label_NumerosMayor&Potencia

""" -------------------------- Funcion Main -------------------------- """
ventana = tk.Tk() 
# objeto tipo ventana de la clase Tkinter
ventana.title("Primera Tarea Programada") 
# Titulo de la ventana
ventana.geometry("700x600")
# tamano de la ventana

labelTitulo(ventana, 200, 20)

labelNumeros(ventana, 20, 70)

labelNumeroMayor(ventana, 20 , 200)

labelNumeroMenor(ventana, 20, 270)

labelNumeroMayorMultiplicado(ventana, 20, 350)

labelNumeroMenorMultiplicado(ventana, 20, 400)

ventana.mainloop()







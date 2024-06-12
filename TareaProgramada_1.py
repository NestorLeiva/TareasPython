import tkinter as tk
#importacion de la clase Tkinter

ventana = tk.Tk() 
# objeto tipo ventana de la clase Tkinter

""" -------------------------- Funciones -------------------------- """
def labelTitulo(ventana, x , y):
    label = tk.Label(ventana, text="Entrada de Numeros a Evaluar", font=("",15))
    label.place(x=x, y=y)
    #label.pack(padx=20, pady=20)

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

def TexBoxNumero_1(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumero1

def TexBoxNumero_2(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumero2

def TexBoxNumero_3(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumero3

def TexBoxNumero_Mayor(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumeroMayor

def TexBoxNumero_Menor(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumeroMenor

def TexBoxNumero_MayorMultiplicado(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumeroMayorMultiplicado

def TexBoxNumero_MayorPotencia(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumeroMayorPotencia

def TexBoxNumero_MenorMultiplicado(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumeroMenorMultiplicado

def TexBoxNumero_MenorPotencia(ventana, x,y):
    Texto = tk.Entry(ventana, width=10)
    Texto.place(x=x, y=y)
#Fin textBoxNumeroMenorPotencia

def BotonProcesar(ventana, x , y):
    boton = tk.Button(ventana, text="Procesar",font=("", 12))
    #accion == command = 
    boton.place(x=x,y=y)
#Boton Calcular Operaciones

def BotonTerminar(ventana, x , y):
    boton = tk.Button(ventana, text="Terminar",font=("", 12))
    #accion == command = 
    boton.place(x=x,y=y)
#terminar la ejecucion del programa

def BotonLimpiar(ventana, x , y):
    boton = tk.Button(ventana, text="Limpiar",font=("", 12))
    #accion == command = 
    boton.place(x=x,y=y)
#Boton Limpiar TextBox


""" -------------------------- Funcion Main -------------------------- """

ventana.title("Primera Tarea Programada") 
# Titulo de la ventana
ventana.geometry("700x500")
# tamano de la ventana

""" *** Llamada de Funciones *** """
labelTitulo(ventana, 200, 20)

labelNumeros(ventana, 100, 120)
TexBoxNumero_1(ventana,350,120)
TexBoxNumero_2(ventana,450,120)
TexBoxNumero_3(ventana,550,120)

BotonProcesar(ventana,350, 150 )
BotonLimpiar(ventana, 450, 150 )

labelNumeroMayor(ventana, 210 , 200)
TexBoxNumero_Mayor(ventana, 350 , 200)

labelNumeroMenor(ventana, 210, 270)
TexBoxNumero_Menor(ventana, 350 , 270)

labelNumeroMayorMultiplicado(ventana, 30, 350)
TexBoxNumero_MayorMultiplicado(ventana, 450 , 350)
TexBoxNumero_MayorPotencia(ventana, 350 , 350)

labelNumeroMenorMultiplicado(ventana, 30, 400)
TexBoxNumero_MenorMultiplicado(ventana,350 , 400)
TexBoxNumero_MenorPotencia(ventana, 450, 400)

BotonTerminar(ventana, 375,450 )


ventana.mainloop()







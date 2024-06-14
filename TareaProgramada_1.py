#from tkinter import * = otra forma de llamar a la libreria Tkinter
import tkinter as tk
#importacion de la clase Tkinter

ventana = tk.Tk() 
# objeto tipo ventana de la clase Tkinter

ventana.title("Prueba")   # Titulo de la ventana
ventana.geometry("700x500") # tamano de la ventana
#------------------------------------ Funciones -----------------------------------------#
def Operaciones():
    print("HolaMundoEstoEsUnaPrueba")
# fin Funcion Operaciones

def LimparTextBox(*TextoWidget):
    for texto in TextoWidget:
        texto.delete(0,"end")
        """ * en el parametro permite una cantidad variable de arguementos
        (0, 'end') borra el contenido de cada Widget desde el primer caracter '0' hasta el ultimo 'end'  """

def CrearTextBox():
    txtNumero1 = tk.Entry(ventana, width=10, justify="center")
    txtNumero1.place(x=350, y=120)
    txtNumero2 = tk.Entry(ventana, width=10, justify="center")
    txtNumero2.place(x=450, y=120)
    txtNumero3 = tk.Entry(ventana, width=10, justify="center")
    txtNumero3.place(x=550, y=120)
    txtNumeroMayor = tk.Entry(ventana, width=10, justify="center")
    txtNumeroMayor.place(x=350, y=200)
    txtNumeroMenor = tk.Entry(ventana, width=10, justify="center")
    txtNumeroMenor.place(x=350, y=270)
    txtNumeroMayorMultiplicado = tk.Entry(ventana, width=10, justify="center")
    txtNumeroMayorMultiplicado.place(x=450, y=350)
    txtNumeroMayorPotencia = tk.Entry(ventana, width=10, justify="center")
    txtNumeroMayorPotencia.place(x=350, y=350)
    txtNumeroMenorMultiplicado = tk.Entry(ventana, width=10, justify="center")
    txtNumeroMenorMultiplicado.place(x=350, y=400)
    txtNumeroMenorPotencia = tk.Entry(ventana, width=10, justify="center")
    txtNumeroMenorPotencia.place(x=450, y=400)

    return txtNumero1, txtNumero2, txtNumero3, txtNumeroMayor, txtNumeroMenor, txtNumeroMayorMultiplicado, txtNumeroMenorMultiplicado, txtNumeroMayorPotencia, txtNumeroMenorPotencia
    # se realiza el retorno de cada label
# fin fincion para crear textBox

def CrearLabel(): 
    lblNumeroMayor = tk.Label(ventana, text="Numero Mayor", font=("",12)).place(x=210,y=200)
    lblNumeroMenor = tk.Label(ventana, text="Numero Menor", font=("",12)).place(x=210,y=270)
    lblNumeroMayorMultiplicado = tk.Label(ventana, text="Numero Mayor multiplicado & en Potencia", font=("",12)).place(x=30,y=350)
    lblNumeroMenorMultiplicado = tk.Label(ventana, text="Numero Menor multiplicado & en Potencia", font=("",12)).place(x=30,y=400) 
    lblTitulo = tk.Label(ventana, text="Entrada de Numeros a Evaluar", font=("",15)).place(x=220, y=50)
    lblInstruccion = tk.Label(ventana,text="Ingrese los 3 numeros a Evaluar", font=("",12)).place(x=100, y=120)   

    return lblNumeroMayor, lblNumeroMenor, lblNumeroMayorMultiplicado, lblNumeroMenorMultiplicado, lblTitulo, lblInstruccion 
    # se realiza el retorno de cada label
# fin fincion para crear Label
#------------------------------------ Fin Funciones -----------------------------------------#

#------------------------------------  Inicio Widget -----------------------------------------#

txtNumero1, txtNumero2, txtNumero3, txtNumeroMayor, txtNumeroMenor, txtNumeroMayorMultiplicado, txtNumeroMenorMultiplicado, txtNumeroMayorPotencia, txtNumeroMenorPotencia = CrearTextBox()
lblNumeroMayor, lblNumeroMenor, lblNumeroMayorMultiplicado, lblNumeroMenorMultiplicado, lblTitulo, lblInstruccion = CrearLabel()
# se crean las variables para cada Label y TextBox y estas son asignadas a las funciones respectivas
#-----------------------------------------------------------------------------#
btnProcesar = tk.Button(ventana, text="Procesar",font=("", 12),command=Operaciones).place(x=350,y=150)

btnLimpiar = btnProcesar = tk.Button(ventana, text="Limpiar",font=("", 12),command=lambda: LimparTextBox(
    txtNumero1, txtNumero2, txtNumero3, txtNumero3, txtNumeroMayor, txtNumeroMenor,
    txtNumeroMayorMultiplicado, txtNumeroMenorMultiplicado, txtNumeroMayorPotencia, txtNumeroMenorPotencia)).place(x=450,y=150)
""" lambda = forma corta de declaracion de funciones pequenas y anonimas. Esta se comporta como una funcion normal. """
btnTerminar = tk.Button(ventana, text="Terminar",font=("", 12), command=exit).place(x=375,y=450)
#------------------------------------ Fin Widget -----------------------------------------#




ventana.mainloop()
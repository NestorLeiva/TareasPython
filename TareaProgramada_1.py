#from tkinter import * = otra forma de llamar a la libreria Tkinter
import tkinter as tk
from tkinter import messagebox
#importacion de la clase Tkinter
ventana = tk.Tk() 
# objeto tipo ventana de la clase Tkinter
ventana.title("Prueba")   # Titulo de la ventana
ventana.geometry("700x500") # tamano de la ventana
#------------------------------------ Funciones -----------------------------------------#
def Operaciones():
    try:
        numero1 = int(txtNumero1.get())
        numero2 = int(txtNumero2.get())
        numero3 = int(txtNumero3.get())

        ListaNumeros = [numero1, numero2, numero3]
        NumRepetidos = set([x for x in ListaNumeros if ListaNumeros.count(x) > 1 ])
        """ lista de comprensión en Python*** se realiza el recorrido con el For,  posterior se realiza un filtrado para incluir 
        los numeros que se repiten mas de 1 vez, posterior devuelve la cantidad de veces que se repite. """

        if not (1 <= numero1 <= 10) or not (1 <= numero2 <= 10) or not (1 <= numero3 <= 10):
            messagebox.showwarning("Tarea Programada # 1", "Los numeros Ingresados deben estar entre 1 y 10")
            LimpiarTextBox(txtNumero1, txtNumero2, txtNumero3) 
            # Invoco a la funcion con los parametro para limpiar los TextBox
            return
        
        if NumRepetidos:
            mensaje = "Numero Repetido es: ", NumRepetidos.pop()
            """El método pop()  borra y retorna el último elemento de una lista. Si no se especifica ningún índice """
            messagebox.showwarning(f"Tarea Programada # 1", mensaje)
            LimpiarTextBox(txtNumero1, txtNumero2, txtNumero3)
            # Invoco a la funcion con los parametro para limpiar los TextBox
            return
                
        #-- encontrar numero mayor --
        Numero_Mayor = max(ListaNumeros)
        #La función max devuelve el máximo valor de un iterable, o el máximo valor de dos o más argumentos
        Numero_Menor = min(ListaNumeros)
        #La función min devuelve el mínimo valor de un iterable, o el mínimo valor de dos o más argumentos.

        #--  Muestro el resultado del numero mayor / Menor -- 
        lblResNumeroMayor.config(text=str(Numero_Mayor))
        # str = se utiliza para representar texto
        lblResNumeroMenor.config(text=str(Numero_Menor))

        Numero_Mayor_Multiplicado = Numero_Mayor
            
        if Numero_Mayor_Multiplicado > 5:
            Numero_Mayor_Multiplicado *= 4
        elif Numero_Mayor_Multiplicado <= 5:
            Numero_Mayor_Multiplicado *= 3

        # *= es equivalente a Numero_Mayor_Multiplicado = Numero_Mayor_Multiplicado 

        lblResNumeroMayorMultiplicado.config(text=str(Numero_Mayor_Multiplicado))
        # impresion del resultado

        Numero_Menor_Multiplicado = Numero_Menor

        if Numero_Menor_Multiplicado <= 5:
            Numero_Menor_Multiplicado *= 2
        elif Numero_Menor_Multiplicado > 5:
            Numero_Menor_Multiplicado *= 1

        lblResNumeroMenorMultiplicado.config(text=str(Numero_Menor_Multiplicado))
         # impresion del resultado

        Numero_Mayor_Potencia = Numero_Mayor
        Numero_Menor_Potencia = Numero_Menor

        lblResNumeroMayorPotencia.config(text=str(Numero_Mayor_Potencia**2))
        lblResNumeroMenorPotencia.config(text=str(Numero_Menor_Potencia**2))

    except ValueError:
        messagebox.showerror("Tarea Programada # 1", "Ingrese Valores Validos")
        LimpiarTextBox(txtNumero1, txtNumero2, txtNumero3)
        # Invoco a la funcion con los parametro para limpiar los TextBox
# fin Funcion Operaciones

def LimpiarTextBox(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")
    """ * en el parametro permite una cantidad variable de arguementos (0, 'end') borra el contenido de cada Widget desde el primer caracter '0' hasta el ultimo 'end'  """

def CrearTextBox():
    txtNumero1 = tk.Entry(ventana, width=10, justify="center", bd=1, relief="solid")
    txtNumero1.place(x=350, y=120)
 #----------------------------------------------------------#
    txtNumero2 = tk.Entry(ventana, width=10, justify="center", bd=1, relief="solid")
    txtNumero2.place(x=450, y=120)
 #----------------------------------------------------------#
    txtNumero3 = tk.Entry(ventana, width=10, justify="center", bd=1, relief="solid")
    txtNumero3.place(x=550, y=120)
#----------------------------------------------------------#

    return txtNumero1, txtNumero2, txtNumero3 
    # se realiza el retorno de cada label
# fin fincion para crear textBox

def CrearLabel(): 
    lblTitulo = tk.Label(ventana, text="Entrada de Numeros a Evaluar", font=("",15)).place(x=220, y=50)
    lblInstruccion = tk.Label(ventana,text="Ingrese los 3 numeros a Evaluar", font=("",12)).place(x=100, y=120)
    lblInstruccion = tk.Label(ventana,text="Los Numeros deden de ser igual o Mayor que 1 y igual o Menor que 10", font=("",8)).place(x=20, y=150)   
    lblNumeroMayor = tk.Label(ventana, text="Numero Mayor", font=("",12)).place(x=210,y=200)
    lblNumeroMenor = tk.Label(ventana, text="Numero Menor", font=("",12)).place(x=210,y=270)
    lblNumeroMayorMultiplicado = tk.Label(ventana, text="Numero Mayor multiplicado & en Potencia", font=("",12)).place(x=30,y=350)
    lblNumeroMenorMultiplicado = tk.Label(ventana, text="Numero Menor multiplicado & en Potencia", font=("",12)).place(x=30,y=400) 
#----------------------------------------------------------#
    lblResNumeroMayor = tk.Label(ventana, text='---', width=10, justify="center", bd=1, relief="solid")
    lblResNumeroMayor.place(x=350, y=200)
#----------------------------------------------------------#
    lblResNumeroMenor = tk.Label(ventana, text='---', width=10, justify="center", bd=1, relief="solid")
    lblResNumeroMenor.place(x=350, y=270)
#----------------------------------------------------------#
    lblResNumeroMayorMultiplicado = tk.Label(ventana, text='---', width=10, justify="center", bd=1, relief="solid")
    lblResNumeroMayorMultiplicado.place(x=350, y=350)
#----------------------------------------------------------#
    lblResNumeroMenorMultiplicado = tk.Label(ventana, text='---', width=10, justify="center", bd=1, relief="solid")
    lblResNumeroMenorMultiplicado.place(x=350, y=400)
#----------------------------------------------------------#
    lblResNumeroMayorPotencia = tk.Label(ventana, text='---', width=10, justify="center", bd=1, relief="solid")
    lblResNumeroMayorPotencia.place(x=450, y=350)
#----------------------------------------------------------#
    lblResNumeroMenorPotencia = tk.Label(ventana, text='---', width=10, justify="center", bd=1, relief="solid")
    lblResNumeroMenorPotencia.place(x=450, y=400)
#----------------------------------------------------------#
    return (lblNumeroMayor, lblNumeroMenor, lblNumeroMayorMultiplicado, lblNumeroMenorMultiplicado, lblTitulo, lblInstruccion, 
        lblResNumeroMayor, lblResNumeroMenor, lblResNumeroMayorMultiplicado, lblResNumeroMenorMultiplicado, lblResNumeroMayorPotencia, lblResNumeroMenorPotencia)
    # se realiza el retorno de cada label
# fin fincion para crear Label
#------------------------------------ Fin Funciones -----------------------------------------#

#------------------------------------  Inicio Widget -----------------------------------------#
txtNumero1, txtNumero2, txtNumero3 = CrearTextBox()

(lblNumeroMayor, lblNumeroMenor, lblNumeroMayorMultiplicado, lblNumeroMenorMultiplicado, lblTitulo, lblInstruccion, 
    lblResNumeroMayor, lblResNumeroMenor, lblResNumeroMayorMultiplicado, lblResNumeroMenorMultiplicado,
    lblResNumeroMayorPotencia, lblResNumeroMenorPotencia) = CrearLabel()
# se crean las variables para cada Label y TextBox y estas son asignadas a las funciones respectivas
#-----------------------------------------------------------------------------#
btnProcesar = tk.Button(ventana, text="Procesar",font=("", 12),command= Operaciones).place(x=450,y=150)

btnLimpiar = btnProcesar = tk.Button(ventana, text="Limpiar",font=("", 12),command=lambda: LimpiarTextBox(
    txtNumero1, txtNumero2, txtNumero3, txtNumero3 )).place(x=550,y=150)
""" lambda = forma corta de declaracion de funciones pequenas y anonimas. Esta se comporta como una funcion normal. """

btnTerminar = tk.Button(ventana, text="Terminar",font=("", 12), command=ventana.quit).place(x=375,y=450)
#------------------------------------ Fin Widget -----------------------------------------#

ventana.mainloop()
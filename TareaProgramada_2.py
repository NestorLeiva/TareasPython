import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
#------------------------------------  Inicio Widget -----------------------------------------#
ventana.title("Calculadora")
ventana.geometry("400x300")
#------------------------------------  Variables Globales -----------------------------------------#
operador = "" # Almacena los numeros y los operadores 
input_text = tk.StringVar() # Actualiza el texto automaticamente
#------------------------------------  Inicio Funciones -----------------------------------------#
def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")

def btnClcik(numero):
    global operador 
    # global permite trabajar con la variable goblal 'operador' 
    operador = operador + str(numero) 
    # concateno el valor 'numero' al final del valor actual del operador. luego se convierte el numero a string antes de concatenarlo
    input_text.set(operador) 
    # actualiza el string dinamicamente con el valor del 'operador' que esta vinculado al txtNumeros 
    # Funcion para llamar al boton(del teclado) y anade el numero a la entrada

def Borrar():
    strEliminar = input_text.get() 
    input_text.set(strEliminar[:-1])
    """obtengo el string y lo asigo a la variable eliminar posterior le seteo el string eliminando el ultimo caracter"""

def LimpiarEntrada(entrada):
    return ''.join(filter(lambda x: x in "0123456789+-*/.", entrada))
    """ limpiar una cadena de texto que representa una expresión matemática, eliminando cualquier carácter que no sea válido para dicha expresión.
    filter = funcion para crear una lista donde el valor devuelto es TRUE. 
    Filter = obtiene 2 argumentos: 1 funcion & 1 iterable
    lambda x: x in '0123456789+-*/.' = verifica que 'x' este dentro del string 
    ''.join = obtiene el iterable y lo convierte en una cadena y une la cadena 
    Este lambda funciona como un bucle for : 'filter' realiza la iteracion. 'x' realiza la comprobacion
    """

def Operaciones():
    global operador
    try:
        operador = LimpiarEntrada(input_text.get()) # se invoca a la funcion para eliminar cualquier caracter no valido.
        opera=str(eval(operador))
        input_text.set(opera)
        # eval = evalua la expresión contenida en operador. El resultado se convierte a una cadena de texto y se asigna a la variable opera. 
        # Luego, este resultado se muestra en algún lugar de la interfaz gráfica a través del método set de input_text.
    except:
        input_text.set("ERROR")
    operador = ""
#------------------------------------  Fin Funciones -----------------------------------------#
#------------------------------------  Inicio Botones -----------------------------------------#
txtNumeros = tk.Entry(ventana, textvariable=input_text, justify="right", bd=2,  relief="solid", font=("", 14))
# agrego un parametro  *textvariable* y se le asigna el valor de la variable gobal 'input_text' realizando asi la union entre el txt y los botones
txtNumeros.grid(row=1, column=1, columnspan=5,padx=5,pady=5, sticky="we")
""" columnspan = cantidad de columnas que puede acumular
sticky = expande el widget dentro de las columnas.//"we" = son combinaciones de las letras n, s, e, w 'puntos cardinales en ingles' """
#------------------------------------ 
btnLimpiar = tk.Button(ventana, text="Limpiar",width=29, justify="center", bd=1, relief="solid", font=("",12), command=lambda:Limpiar(txtNumeros))
# el lambda en este caso llama a la funcion limpiar y este limpia el txtNumeros
btnDivicion = tk.Button(ventana, text="/",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik('/'))
# el lambda en este caso llama a la funcion BtnClick que tiene por parametro el operador '/' de esta manera funciona solamente para esta tecla
btnNum_7 = tk.Button(ventana, text="7",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(7))
btnNum_8 = tk.Button(ventana, text="8",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(8))
btnNum_9 = tk.Button(ventana, text="9",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(9))
btnMulti = tk.Button(ventana, text="*",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik('*'))
#------------------------------------ 
btnNum_4 = tk.Button(ventana, text="4",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(4))
btnNum_5 = tk.Button(ventana, text="5",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(5))
btnNum_6 = tk.Button(ventana, text="6",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(6))
btnResta = tk.Button(ventana, text="-",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik('-'))
#------------------------------------ 
btnNum_1 = tk.Button(ventana, text="1",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(1))
btnNum_2 = tk.Button(ventana, text="2",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(2))
btnNum_3 = tk.Button(ventana, text="3",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(3))
btnSuma = tk.Button(ventana, text="+",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik('+'))
#------------------------------------ 
btnNum_0 = tk.Button(ventana, text="0",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik(0))
btnPunto = tk.Button(ventana, text=".",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:btnClcik('.'))
btnBorrar = tk.Button(ventana, text="Borrar",width=8, justify="center", bd=1, relief="solid", font=("",12), command=Borrar)
btnResrul = tk.Button(ventana, text="=",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:Operaciones())
""" Sin lambda: Usas la función directamente cuando no necesitas pasarle argumentos adicionales. Es simple y directo.
Con lambda: Usas lambda para crear una función que llama a otra función con los argumentos específicos que necesitas. """
#------------------------------------  Fin Botones -----------------------------------------#
btnLimpiar.grid(row = 2, column = 0, columnspan=4, padx = 5, pady = 5)
btnDivicion.grid(row = 2, column = 4, columnspan=4, padx = 5, pady = 5)
btnNum_7.grid(row = 3, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_8.grid(row = 3, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_9.grid(row = 3, column = 3, columnspan=1, padx = 5, pady = 5)
btnMulti.grid(row = 3, column = 4, columnspan=1, padx = 5, pady = 5)
btnNum_4.grid(row = 4, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_5.grid(row = 4, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_6.grid(row = 4, column = 3, columnspan=1, padx = 5, pady = 5)
btnResta.grid(row = 4, column = 4, columnspan=1, padx = 5, pady = 5)
btnNum_1.grid(row = 5, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_2.grid(row = 5, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_3.grid(row = 5, column = 3, columnspan=1, padx = 5, pady = 5)
btnSuma.grid(row = 5, column = 4, columnspan=1, padx = 5, pady = 5)
btnNum_0.grid(row = 6, column = 1, columnspan=1, padx = 5, pady = 5)
btnPunto.grid(row = 6, column = 2, columnspan=1, padx = 5, pady = 5)
btnBorrar.grid(row = 6, column = 3, columnspan=1, padx = 5, pady = 5)
btnResrul.grid(row = 6, column = 4, columnspan=1, padx = 5, pady = 5)
ventana.mainloop()
#------------------------------------  Fin Widget -----------------------------------------#
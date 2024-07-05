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

def BtnClcik(numero):
    global operador 
    # global permite trabajar con la variable goblal 'operador' 
    operador = operador + str(numero) 
    # concateno el valor 'numero' al final del valor actual del operador. luego se convierte el numero a string antes de concatenarlo
    input_text.set(operador) 
    # actualiza el string dinamicamente con el valor del 'operador' que esta vinculado al txtNumeros 
    # Funcion para llamar al boton(del teclado) y anade el numero a la entrada

def Borrar():
    global operador
    operador = operador[:-1]
    input_text.set(operador)
#------------------------------------  Fin Funciones -----------------------------------------#
#------------------------------------  Inicio Botones -----------------------------------------#
txtNumeros = tk.Entry(ventana, textvariable=input_text, justify="left", bd=2, relief="solid", font=("", 14))
# agrego un parametro  *textvariable* y se le asigna el valor de la variable gobal 'input_text' realizando asi la union entre el txt y los botones
txtNumeros.grid(row=1, column=1, columnspan=5,padx=5,pady=5, sticky="we")
""" columnspan = cantidad de columnas que puede acumular
sticky = expande el widget dentro de las columnas.//"we" = son combinaciones de las letras n, s, e, w 'puntos cardinales en ingles' """
#------------------------------------ 
btnNum_Limpiar = tk.Button(ventana, text="Limpiar",width=30, justify="center", bd=1, relief="solid", font=("",12), command=lambda:Limpiar(txtNumeros))
# el lambda en este caso llama a la funcion limpiar y este limpia el txtNumeros
btnNum_Limpiar.grid(row = 2, column = 0, columnspan=4, padx = 5, pady = 5)
btnNum_Divicion = tk.Button(ventana, text="/",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik('/'))
# el lambda en este caso llama a la funcion BtnClick que tiene por parametro el operador '/' de esta manera funciona solamente para esta tecla
btnNum_Divicion.grid(row = 2, column = 4, columnspan=4, padx = 5, pady = 5)
#------------------------------------ 
btnNum_7 = tk.Button(ventana, text="7",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(7))
btnNum_7.grid(row = 3, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_8 = tk.Button(ventana, text="8",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(8))
btnNum_8.grid(row = 3, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_9 = tk.Button(ventana, text="9",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(9))
btnNum_9.grid(row = 3, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Multi = tk.Button(ventana, text="*",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik('*'))
btnNum_Multi.grid(row = 3, column = 4, columnspan=1, padx = 5, pady = 5)
#------------------------------------ 
btnNum_4 = tk.Button(ventana, text="4",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(4))
btnNum_4.grid(row = 4, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_5 = tk.Button(ventana, text="5",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(5))
btnNum_5.grid(row = 4, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_6 = tk.Button(ventana, text="6",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(6))
btnNum_6.grid(row = 4, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Resta = tk.Button(ventana, text="-",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik('-'))
btnNum_Resta.grid(row = 4, column = 4, columnspan=1, padx = 5, pady = 5)
#------------------------------------ 
btnNum_1 = tk.Button(ventana, text="1",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(1))
btnNum_1.grid(row = 5, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_2 = tk.Button(ventana, text="2",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(2))
btnNum_2.grid(row = 5, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_3 = tk.Button(ventana, text="3",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(3))
btnNum_3.grid(row = 5, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Suma = tk.Button(ventana, text="+",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik('+'))
btnNum_Suma.grid(row = 5, column = 4, columnspan=1, padx = 5, pady = 5)
#------------------------------------ 
btnNum_0 = tk.Button(ventana, text="0",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik(0))
btnNum_0.grid(row = 6, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_Punto = tk.Button(ventana, text=".",width=8, justify="center", bd=1, relief="solid", font=("",12), command=lambda:BtnClcik('.'))
btnNum_Punto.grid(row = 6, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_Borrar = tk.Button(ventana, text="Borrar",width=8, justify="center", bd=1, relief="solid", font=("",12))
btnNum_Borrar.grid(row = 6, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Resrultado = tk.Button(ventana, text="=",width=8, justify="center", bd=1, relief="solid", font=("",12))
btnNum_Resrultado.grid(row = 6, column = 4, columnspan=1, padx = 5, pady = 5)

#------------------------------------  Fin Botones -----------------------------------------#
ventana.mainloop()
#------------------------------------  Fin Widget -----------------------------------------#
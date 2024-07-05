import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
#------------------------------------  Inicio Widget -----------------------------------------#
ventana.title("Calculadora")
ventana.geometry("325x300")
#------------------------------------  Variables Globales -----------------------------------------#


#------------------------------------  Inicio Funciones -----------------------------------------#

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def divicion(a,b):
    if b == 0:
        return messagebox.showerror("Divicion por Cero")
    else:
        return a / b
def multiplicacion(a,b):
    return a * b
def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")

#------------------------------------  Fin Funciones -----------------------------------------#
#------------------------------------  Inicio Botones -----------------------------------------#
txtNumeros = tk.Entry(ventana, justify="left", bd=2, relief="solid",font=("",14))
txtNumeros.grid(row=1, column=1, columnspan=5,padx=5,pady=5, sticky="we")
""" columnspan = cantidad de columnas que puede acumular
sticky = expande el widget dentro de las columnas. 
    "we" = son combinaciones de las letras n, s, e y w 'puntos cardinales en ingles'
"""
#------------------------------------ 
btnNum_Limpiar = tk.Button(ventana, text="Limpiar",width=30, justify="center", bd=1, relief="solid", command=lambda:Limpiar(txtNumeros))
btnNum_Limpiar.grid(row = 2, column = 0, columnspan=4, padx = 5, pady = 5)
btnNum_Divicion = tk.Button(ventana, text="/",width=8, justify="center", bd=1, relief="solid")
btnNum_Divicion.grid(row = 2, column = 4, columnspan=4, padx = 5, pady = 5)
#------------------------------------ 
btnNum_7 = tk.Button(ventana, text="7",width=8, justify="center", bd=1, relief="solid")
btnNum_7.grid(row = 3, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_8 = tk.Button(ventana, text="8",width=8, justify="center", bd=1, relief="solid")
btnNum_8.grid(row = 3, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_9 = tk.Button(ventana, text="9",width=8, justify="center", bd=1, relief="solid")
btnNum_9.grid(row = 3, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Multi = tk.Button(ventana, text="*",width=8, justify="center", bd=1, relief="solid")
btnNum_Multi.grid(row = 3, column = 4, columnspan=1, padx = 5, pady = 5)
#------------------------------------ 
btnNum_4 = tk.Button(ventana, text="4",width=8, justify="center", bd=1, relief="solid")
btnNum_4.grid(row = 4, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_5 = tk.Button(ventana, text="5",width=8, justify="center", bd=1, relief="solid")
btnNum_5.grid(row = 4, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_6 = tk.Button(ventana, text="6",width=8, justify="center", bd=1, relief="solid")
btnNum_6.grid(row = 4, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Resta = tk.Button(ventana, text="-",width=8, justify="center", bd=1, relief="solid")
btnNum_Resta.grid(row = 4, column = 4, columnspan=1, padx = 5, pady = 5)
#------------------------------------ 
btnNum_1 = tk.Button(ventana, text="1",width=8, justify="center", bd=1, relief="solid")
btnNum_1.grid(row = 5, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_2 = tk.Button(ventana, text="2",width=8, justify="center", bd=1, relief="solid")
btnNum_2.grid(row = 5, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_3 = tk.Button(ventana, text="3",width=8, justify="center", bd=1, relief="solid")
btnNum_3.grid(row = 5, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Suma = tk.Button(ventana, text="+",width=8, justify="center", bd=1, relief="solid")
btnNum_Suma.grid(row = 5, column = 4, columnspan=1, padx = 5, pady = 5)
#------------------------------------ 
btnNum_0 = tk.Button(ventana, text="0",width=8, justify="center", bd=1, relief="solid") 
btnNum_0.grid(row = 6, column = 1, columnspan=1, padx = 5, pady = 5)
btnNum_Punto = tk.Button(ventana, text=".",width=8, justify="center", bd=1, relief="solid")
btnNum_Punto.grid(row = 6, column = 2, columnspan=1, padx = 5, pady = 5)
btnNum_Borrar = tk.Button(ventana, text="Borrar",width=8, justify="center", bd=1, relief="solid")
btnNum_Borrar.grid(row = 6, column = 3, columnspan=1, padx = 5, pady = 5)
btnNum_Resrultado = tk.Button(ventana, text="=",width=8, justify="center", bd=1, relief="solid")
btnNum_Resrultado.grid(row = 6, column = 4, columnspan=1, padx = 5, pady = 5)
#------------------------------------ 

#------------------------------------  Fin Botones -----------------------------------------#
ventana.mainloop()
#------------------------------------  Fin Widget -----------------------------------------#
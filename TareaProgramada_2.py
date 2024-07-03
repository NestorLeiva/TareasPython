import tkinter as  tk
ventana = tk.Tk()
#------------------------------------  Inicio Widget -----------------------------------------#
ventana.title("Calculadora")
ventana.geometry("500x500")
#------------------------------------  Inicio Botones -----------------------------------------#
txtNumeros = tk.Entry(ventana,width=30, justify="center", bd=1, relief="solid",font=("",15)).place(x= 75 , y=100)

btnNum_0 = tk.Button(ventana, text="0",width=8, justify="center", bd=1, relief="solid").place(x= 75 , y=350)
btnNum_1 = tk.Button(ventana, text="1",width=8, justify="center", bd=1, relief="solid").place(x= 75 , y=300)
btnNum_2 = tk.Button(ventana, text="2",width=8, justify="center", bd=1, relief="solid").place(x= 160 , y=300)
btnNum_3 = tk.Button(ventana, text="3",width=8, justify="center", bd=1, relief="solid").place(x= 250 , y=300)
btnNum_4 = tk.Button(ventana, text="4",width=8, justify="center", bd=1, relief="solid").place(x= 75 , y=250)
btnNum_5 = tk.Button(ventana, text="5",width=8, justify="center", bd=1, relief="solid").place(x= 160 , y=250)
btnNum_6 = tk.Button(ventana, text="6",width=8, justify="center", bd=1, relief="solid").place(x= 250 , y=250)
btnNum_7 = tk.Button(ventana, text="7",width=8, justify="center", bd=1, relief="solid").place(x= 75 , y=200)
btnNum_8 = tk.Button(ventana, text="8",width=8, justify="center", bd=1, relief="solid").place(x= 160 , y=200)
btnNum_9 = tk.Button(ventana, text="9",width=8, justify="center", bd=1, relief="solid").place(x= 250 , y=200)
btnNum_Punto = tk.Button(ventana, text=".",width=8, justify="center", bd=1, relief="solid").place(x= 160 , y=350)
btnNum_Resrultado = tk.Button(ventana, text="=",width=8, justify="center", bd=1, relief="solid").place(x= 340 , y=350)
btnNum_Limpiar = tk.Button(ventana, text="Limpiar",width=33, justify="center", bd=1, relief="solid").place(x= 75 , y=150)
btnNum_Borrar = tk.Button(ventana, text="Borrar",width=8, justify="center", bd=1, relief="solid").place(x= 250 , y=350)

btnNum_Resta = tk.Button(ventana, text="-",width=8, justify="center", bd=1, relief="solid").place(x= 340 , y=150)
btnNum_Suma = tk.Button(ventana, text="+",width=8, justify="center", bd=1, relief="solid").place(x= 340 , y=200)
btnNum_Multiplicacion = tk.Button(ventana, text="*",width=8, justify="center", bd=1, relief="solid").place(x= 340 , y=250)
btnNum_Divicion = tk.Button(ventana, text="/",width=8, justify="center", bd=1, relief="solid").place(x= 340 , y=300)

#------------------------------------  Fin Botones -----------------------------------------#
ventana.mainloop()
#------------------------------------  Fin Widget -----------------------------------------#
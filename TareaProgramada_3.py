import  tkinter as tk

ventana = tk.Tk()

ventana.geometry("300x220")
ventana.title("Consulta de Informacion")
#----------------------------------------------------------------------------------------------------------------------------------#
lblentrada = tk.Label(ventana, text="Ingrese el dato a consultar",width=25, justify="center", bd=1, relief="solid", font=("",12))
lblentrada.grid(row = 1, column = 1, columnspan=5, padx = 5, pady = 5,sticky="we")
txtEntrada = tk.Entry(ventana,  justify="center", bd=2,  relief="solid", font=("", 14))
txtEntrada.focus()
txtEntrada.grid(row = 2, column = 1, columnspan=5, padx = 5, pady = 5,sticky="we")
#----------------------------------------------------------------------------------------------------------------------------------#
btnConsultar = tk.Button(ventana, text="Consultar:",width=15, justify="right", bd=3, relief="solid", font=("",12))
btnConsultar.grid(row = 3, column = 1, columnspan=4, padx = 5, pady = 5,sticky="we")
#----------------------------------------------------------------------------------------------------------------------------------#
lblNombre = tk.Label(ventana, text="Nombre:",width=15, justify="right", bd=1, relief="solid", font=("",12))
lblNombre.grid(row = 4, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")

lblProvincia = tk.Label(ventana, text="Provincia",width=15, justify="right", bd=1, relief="solid", font=("",12))
lblProvincia.grid(row = 5, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")

lblCanton = tk.Label(ventana, text="Canton",width=15, justify="right", bd=1, relief="solid", font=("",12))
lblCanton.grid(row = 6, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")
#----------------------------------------------------------------------------------------------------------------------------------#
lblNombreRes = tk.Label(ventana, width=15, justify="right", bd=1, relief="solid", font=("",12))
lblNombreRes.grid(row = 4, column = 2, columnspan=1, padx = 5, pady = 5,sticky="we")

lblProvinciaRes = tk.Label(ventana, width=15, justify="right", bd=1, relief="solid", font=("",12))
lblProvinciaRes.grid(row = 5, column = 2, columnspan=1, padx = 5, pady = 5,sticky="we")

lblCantonRes = tk.Label(ventana, width=15, justify="right", bd=1, relief="solid", font=("",12))
lblCantonRes.grid(row = 6, column = 2, columnspan=1, padx = 5, pady = 5,sticky="we")
ventana.mainloop()
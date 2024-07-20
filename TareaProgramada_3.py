import  tkinter as tk
from tkinter import messagebox 
ventana = tk.Tk()

ventana.geometry("400x460")
ventana.title("Consulta de Informacion")
input_text = tk.StringVar()

def Limpiar(*TextoWidget):
    for texto in TextoWidget: texto.delete(0,"end")



def Operacion():
    try:
        MiTabla = [["Nestor","Leiva", "Villalobos"],[35,"Mayo", 1989],["Cartago","Occidental", "Calle 50"]]
        MiTabla1 = [["Juan","Castro", "Rojas"],[25,"Enero", 1990],["San Jose","Desamparados", "Calle 50"]]
        indice = int(txtEntradaIndice.get())
        nombre = (input_text.get().strip()).capitalize() # .strip elimina los espacios en blanco

        if indice == 1 :
            lblNombreRes.config(text=str(MiTabla[0][0]))
            lblProvinciaRes.config(text=str(MiTabla[2][0]))
            lblCantonRes.config(text=str(MiTabla[2][1]))
        elif indice == 2:
            lblNombreRes.config(text=str(MiTabla1[0][0]))
            lblProvinciaRes.config(text=str(MiTabla1[2][0]))
            lblCantonRes.config(text=str(MiTabla1[2][1]))
        else:
                messagebox.showerror("Tarea 3", "Numero de Persona No Encontrado")
                    
        if nombre == MiTabla[0][0] :
            lblNombreRes.config(text=str(MiTabla[0][0]))
            lblProvinciaRes.config(text=str(MiTabla[2][0]))
            lblCantonRes.config(text=str(MiTabla[2][1]))
        elif nombre == MiTabla1[0][0]:
            lblNombreRes.config(text=str(MiTabla1[0][0]))
            lblProvinciaRes.config(text=str(MiTabla1[2][0]))
            lblCantonRes.config(text=str(MiTabla1[2][1]))
        else:
                messagebox.showerror("Tarea 3", "Nombre de Persona No Encontrado")

        Limpiar(txtEntradaNombre, txtEntradaIndice)
    except ValueError as e:
        Limpiar(txtEntradaNombre, txtEntradaIndice)
        messagebox.showerror("Tarea Programada 3", "Ingrese valores validos en los campos")
   
#----------------------------------------------------------------------------------------------------------------------------------#
lblentrada = tk.Label(ventana, text="Ingrese el dato a consultar",width=25, justify="center", bd=1, relief="solid", font=("",12))
lblentrada.grid(row = 1, column = 1, columnspan=3, padx = 5, pady = 5,sticky="we")
#----------------------------------------------------------------------------------------------------------------------------------#
lblConsultarNombre = tk.Label(ventana, text="Consultar por Nombre:",width=15, justify="right", bd=3, relief="solid", font=("",10))
lblConsultarNombre.grid(row = 2, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")

txtEntradaNombre = tk.Entry(ventana, textvariable=input_text, justify="center", bd=2,  relief="solid", font=("", 14))
txtEntradaNombre.focus()
txtEntradaNombre.grid(row = 2, column = 2, columnspan=2, padx = 5, pady = 5,sticky="we")

lblConsultarIndice = tk.Label(ventana, text="Consultar por Indice:",width=15, justify="right", bd=3, relief="solid", font=("",10))
lblConsultarIndice.grid(row = 4, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")

txtEntradaIndice = tk.Entry(ventana,  justify="center", bd=2,  relief="solid", font=("", 14))
txtEntradaIndice.grid(row = 4, column = 2, columnspan=2, padx = 5, pady = 5,sticky="we")
#----------------------------------------------------------------------------------------------------------------------------------#
btnConsultar = tk.Button(ventana,text="Consultar",  justify="center", bd=2,  relief="solid", font=("", 14), command=Operacion)
btnConsultar.grid(row = 5, column = 1, columnspan=4, padx = 5, pady = 5,sticky="we")
#----------------------------------------------------------------------------------------------------------------------------------#
lblNombre = tk.Label(ventana, text="Nombre:",width=15, justify="right", bd=1, relief="solid", font=("",12))
lblNombre.grid(row = 6, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")

lblProvincia = tk.Label(ventana, text="Provincia",width=15, justify="right", bd=1, relief="solid", font=("",12))
lblProvincia.grid(row = 7, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")

lblCanton = tk.Label(ventana, text="Canton",width=15, justify="right", bd=1, relief="solid", font=("",12))
lblCanton.grid(row = 8, column = 1, columnspan=1, padx = 5, pady = 5,sticky="we")
#----------------------------------------------------------------------------------------------------------------------------------#
lblNombreRes = tk.Label(ventana, width=15, justify="right", bd=1, relief="solid", font=("",12))
lblNombreRes.grid(row =6, column = 2, columnspan=2, padx = 5, pady = 5,sticky="we")

lblProvinciaRes = tk.Label(ventana, width=15, justify="right", bd=1, relief="solid", font=("",12))
lblProvinciaRes.grid(row = 7, column = 2, columnspan=2, padx = 5, pady = 5,sticky="we")

lblCantonRes = tk.Label(ventana, width=15, justify="right", bd=1, relief="solid", font=("",12))
lblCantonRes.grid(row = 8, column = 2, columnspan=2, padx = 5, pady = 5,sticky="we")
ventana.mainloop()
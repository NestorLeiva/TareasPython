import pyodbc
from tkinter import messagebox

server = "NESTORPC\\NESTOR"
database = "progra 3"

class Conexion():
    conn = None # variable global para la conexion
    def LoginSQL(usuario, contrasena):
        try:
            if usuario and contrasena:
                Conexion.conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={usuario};PWD={contrasena};TrustServerCertificate=yes;')
                print("conexion SQL exitosa", usuario)
                messagebox.showinfo("Tarea Programada 5", f'Login Exitoso {usuario}')
                return True
        except pyodbc.Error as e:
            messagebox.showerror("Tarea Programada 5", f'Error en el Login: {e}')
            return False

    def CerrarSQL():
        try:
            if Conexion.conn:
                Conexion.conn.close()
                print('Se realizo el cierre de la Conexion')
                messagebox.showinfo("Tarea Programada 5", "Conexión cerrada correctamente")
                Conexion.conn = None
            else:
                messagebox.showinfo("Tarea Programada 5", "No hay conexión para cerrar")

        except pyodbc.Error as e:
            messagebox.showerror("Tarea Programada 5", f'Error al cerrar la conexión: {e}')

class MetodosSQL():
    def leerSQL():
        pass
    def EscribirSQL():
        pass
    def ActualizarSQL():
        pass
    def EliminarSQL():
        pass
    
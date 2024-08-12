import pyodbc
from tkinter import messagebox

class ConexionSQL:
    __Server__ = "NESTORPC\\NESTOR"
    __DataBase__ ="Progra3Cajero"
    __conn__ = None
    def LoginSQL(usuario, contrasena):
        try:
            if usuario and contrasena:
                ConexionSQL.__conn__ = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};' +
                    f'SERVER={ConexionSQL.__Server__};' +
                    f'DATABASE={ConexionSQL.__DataBase__};' +
                    f'UID={usuario};PWD={contrasena};' +
                    'TrustServerCertificate=yes;')
                print("ConexionSQL exitosa", usuario)
                messagebox.showinfo("Tarea Programada 6", f'Login Exitoso : {usuario}')
                return True
            else:
                messagebox.showwarning("Tarea Programada 6", 'Usuario / Contrasena Incorrecto')
                return False
        except pyodbc.Error as e:
            messagebox.showerror("Tarea Programada 6", 'Usuario / Contrasena Incorrecto. \n Intente de nuevo')
            print(f'Error con la ConexionSQL :{e}')
            return False
    # Fin LoginSQL

    def CerrarSQL():
        try:
            if ConexionSQL.__conn__:
                ConexionSQL.__conn__.close()
                print('ConexionSQL Finalizada con exito')
                ConexionSQL.__conn__ = None
            else:
                print('No existe una conexion para cerrar')
        except pyodbc.Error as e:
            print(f'Error al cerrar la conexionSQL {e}')
            pass
    # Fin CerrarSQL
# Fin class ConexionSQL
class MetodosSQL:
    pass
# Fin class MetodosSQL
#-----------------------------------------------------------------------------------------#
def Prueba():
    if ConexionSQL.LoginSQL(usuario="NestorC", contrasena="nestor10"):
        print('hola mundo: estoy conectado')
    ConexionSQL.CerrarSQL()
#Prueba()

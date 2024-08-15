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
                print(f"ConexionSQL exitosa, __{usuario}__")
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
    def ObtenerUsuario(self, usuario):
        try:
            cursor = ConexionSQL.__conn__.cursor()
            queryObtenerUsuario = """ SELECT * FROM Usuario WHERE usuario = ?"""
            cursor.execute(queryObtenerUsuario,(usuario,))
            
            DatosUsuario = cursor.fetchone()

            if DatosUsuario:
                self.cod_usuario = DatosUsuario[0] # alamaceno los datos obtenidos
                print(f'Datos del Usuairo :',DatosUsuario)
                return DatosUsuario
            else: 
                print(f'_{usuario}_, No encontrado')
                return None
            
        except pyodbc.Error as e:
            print(f'Error al Obtener el Usuario: __{e}__')
        finally:
            cursor.close()
    # Metodo Obtener Datos

    def ConsultaSaldo(self):
        try:
            cursor = ConexionSQL.__conn__.cursor()
            queryConsultaSaldo = """ SELECT saldo_c FROM Cuenta WHERE cod_usuario_c = ?"""
            cursor.execute(queryConsultaSaldo,(self.cod_usuario,)) # paso los datos obtenidos del metodo ObtenerUsuario
            DatosSaldo = cursor.fetchone()

            if DatosSaldo:
                print(f'Saldo es : _{DatosSaldo[0]}_')
                return DatosSaldo[0]
            else:
                print('Saldo No Encontrado')
        except pyodbc.Error as e:
            print(f'Error al Consultar el Saldo {e}')
        finally:
            cursor.close()
    #Metodo Consultar Saldo
        
        
# Fin class MetodosSQL
#-----------------------------------------------------------------------------------------#
def Prueba():
    metodo_sql = MetodosSQL()
    if ConexionSQL.LoginSQL(usuario= "NestorCA", contrasena="nestor10"):
        metodo_sql.ObtenerUsuario(usuario='NestorCA')
        metodo_sql.ConsultaSaldo()
        ConexionSQL.CerrarSQL()
Prueba()
#phantonsita
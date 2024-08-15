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
    # por que ella es tan hermosa xP
    def RealizarDeposito(self, monto):
        try:
            cursor = ConexionSQL.__conn__.cursor()
            queryDeposito = """UPDATE Cuenta SET saldo_c = ? WHERE cod_usuario_c = ?"""
            if (monto >= 1): # valido que el monto sea mayor a 1
                saldoActual = self.ConsultaSaldo() # obtengo el Saldo
                if saldoActual is not None :
                    nuevoSaldo = saldoActual + monto # realizo el aumento del saldo
                    print(f'Saldo Anterior: _{saldoActual}_, Nuevo Saldo : _{nuevoSaldo}_')
                    #-----------------------------------------------------------------------------#
                    cursor.execute(queryDeposito, (nuevoSaldo, self.cod_usuario)) 
                    ConexionSQL.__conn__.commit() # aplico los cambios
                    print(f'Saldo Actualizado :_{nuevoSaldo}_')
                    messagebox.showinfo('Tarea Programada 6', 'Deposito Realizado con Exito')
                else:
                    print('Error al realizar el Deposito')
                    messagebox.showerror('Tarea Programada 6', 'Error al Realizar el Deposito')
                    return nuevoSaldo # se devuelve el saldo SI NO se realiza el deposito 
            else:
                print('Monto Invalido')
                messagebox.showerror('Tarea Programada 6', 'Monto Invalido ')
                return None # devuelve NONE si no se realiza el depostito
        except pyodbc.Error as e:
            ConexionSQL.__conn__.rollback()
            print(f'Error al realizar el deposito__{e}__')
        finally:
            cursor.close()
    # Metodo Realizar depostio
# Fin class MetodosSQL
#-----------------------------------------------------------------------------------------#
def Prueba():
    metodo_sql = MetodosSQL()
    if ConexionSQL.LoginSQL(usuario= "NestorCA", contrasena="nestor10"):
        metodo_sql.ObtenerUsuario(usuario='NestorCA')
        metodo_sql.ConsultaSaldo()
        metodo_sql.RealizarDeposito(1)
        ConexionSQL.CerrarSQL()
Prueba()
#phantonsita
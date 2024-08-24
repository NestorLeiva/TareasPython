import pyodbc
import datetime as dt
from tkinter import messagebox

class ConexionSQL:
    #__Server__ = "NESTORPC\\NESTOR"    #instancia Windows
    __Server__ = "localhost"            #instancia ubuntu
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
#-----------------------------------------------------------------------------------------#
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

    def ConsultaSaldo(self,):
        try:
            cursor = ConexionSQL.__conn__.cursor()
            queryConsultaSaldo = """ SELECT saldo_c FROM Cuenta WHERE cod_usuario_c = ?"""
            cursor.execute(queryConsultaSaldo,(self.cod_usuario,)) # paso los datos obtenidos del metodo ObtenerUsuario
            DatosSaldo = cursor.fetchone()

            if DatosSaldo:
                print(f'Consulta Saldo es : _{DatosSaldo[0]}_')
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
                    print(f'Saldo Anterior: _{saldoActual}_ Nuevo Saldo : _{nuevoSaldo}_')
                    #-----------------------------------------------------------------------------#
                    cursor.execute(queryDeposito, (nuevoSaldo, self.cod_usuario)) 
                    ConexionSQL.__conn__.commit() # aplico los cambios
                    print(f'Saldo Deposito Actualizado :_{nuevoSaldo}_')
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

    def RealizarRetiro(self, monto):
        try:
            cursor = ConexionSQL.__conn__.cursor()
            queryRetiro = """UPDATE Cuenta SET saldo_c = ? WHERE cod_usuario_c = ?"""
            saldoActual = self.ConsultaSaldo() # obtengo el Saldo
            if saldoActual is not None : # Valid que el monto a retirar sea >=  al saldo actual
                if (monto  <= saldoActual ): # valido que el monto sea mayor a 1
                    nuevoSaldo = saldoActual - monto # realizo el aumento del saldo
                    print(f'Saldo Anterior: _{saldoActual}_, Nuevo Saldo : _{nuevoSaldo}_')
                    #-----------------------------------------------------------------------------#
                    cursor.execute(queryRetiro, (nuevoSaldo, self.cod_usuario)) 
                    ConexionSQL.__conn__.commit() # aplico los cambios
                    print(f'Saldo Retiro Actualizado :_{nuevoSaldo}_')
                    messagebox.showinfo('Tarea Programada 6', 'Retiro Realizado con Exito')
                    return nuevoSaldo # se devuelve el saldo SI NO se realiza el deposito 
                else:
                    print('Error al realizar el Retiro')
                    messagebox.showerror('Tarea Programada 6', 'Error al Realizar el Retiro')
            else:
                print('Monto Invalido')
                messagebox.showerror('Tarea Programada 6', 'Monto Invalido ')
            return None  # Devolver None si no se realiza el retiro
        except pyodbc.Error as e:
            ConexionSQL.__conn__.rollback()
            print(f'Error al realizar el deposito__{e}__')
        finally:
            cursor.close()
    # Metodo Realizar depostio
    #cod_mov_a=1,cod_cajero=2 
    def RealizarAuditoria(self, cod_mov_a,cod_cajero ):#parametros al otro lado

        fecha = dt.datetime.now() # obtengo la fecha del dia
        try:
            cursor = ConexionSQL.__conn__.cursor()
            queryAuditoria = """ INSERT INTO Auditoria (cod_usuario_a, movimiento_a, fecha_mov_a, cod_cajero_a) VALUES (?,?, ?,?) """

            cursor.execute(queryAuditoria, (self.cod_usuario,cod_mov_a,fecha,cod_cajero))

            ConexionSQL.__conn__.commit()
            print('*** Auditoria Realizada con Exito ***')
        except pyodbc.Error as e:
            print(f' Error al Realizar la Auditoria: __ {e}  __')
            ConexionSQL.__conn__.rollback()
            pass
        finally:
            cursor.close()
    # Metodo Realizar Auditoria

    def ConsutaCajero(self, cod_cajero):
        try:
            cursor = ConexionSQL.__conn__.cursor()
            queryCajero = """SELECT estado FROM Cajero WHERE cod_cajero = ?"""
            cursor.execute(queryCajero, (cod_cajero,))
            row = cursor.fetchone()
            if row:
                self.estado = row[0]
                print(f"El estado del cajero {cod_cajero} es {self.estado}.")
                return self.estado
            else:
                print(f"No se encontró el cajero con el código {cod_cajero}.")
                return None    
        except pyodbc.Error as e:
            print(f'Error al realizar la consulta del cajero {cod_cajero}: {e}')
            return None
        finally:
            cursor.close()
    # Metodo Realizar Consulta Cajero

    def MovimientoCajero(self, cod_cajero, nuevo_estado):
        try:
            cursor = ConexionSQL.__conn__.cursor()
            
            # Consulta el estado actual del cajero
            estado_actual = self.ConsutaCajero(cod_cajero)
            if estado_actual is None:
                print(f"No se pudo consultar el estado del cajero con código {cod_cajero}.")
                return
            
            # Validar si el cajero está Libre para permitir cambios
            if estado_actual :
                # Cambia el estado del cajero
                queryCambioEstado = """ UPDATE Cajero SET estado = ? WHERE cod_cajero = ? """
                cursor.execute(queryCambioEstado, (nuevo_estado, cod_cajero,))
                ConexionSQL.__conn__.commit()
                print(f"El estado del cajero {cod_cajero} se ha cambiado a {nuevo_estado}.")
                messagebox.showinfo('Tarea Programada 6', 'Se Realizo el Cambio \n de Estado Correctamente')
            else:
                print(f"No se puede realizar el cambio de estado. El cajero {cod_cajero} esta en estado {estado_actual}.")
        except pyodbc.Error as e:
            print(f"Error al realizar el cambio de estado: {e}")
            ConexionSQL.__conn__.rollback()
        finally:
            cursor.close()


# Fin class MetodosSQL
#-----------------------------------------------------------------------------------------#
def Prueba():
    usuario = "NestorCA "
    contrasena ="Nestor_10*"
    usuarioBD = "NestorCa"
    #usuarioBD = "NestorCA"
    #usuario = "NestorCA" 
    #contrasena = 'nestor10' 
    metodo_sql = MetodosSQL()
    if ConexionSQL.LoginSQL(usuario= usuario, contrasena= contrasena):
        metodo_sql.ObtenerUsuario(usuario=usuarioBD)
        metodo_sql.ConsultaSaldo()
        metodo_sql.RealizarDeposito(2350)
        #metodo_sql.RealizarRetiro(2000)
        #metodo_sql.ConsutaCajero(cod_cajero=1) 
        #metodo_sql.MovimientoCajero(cod_cajero=1, nuevo_estado='L') 
        #metodo_sql.MovimientoCajero(cod_cajero=2, nuevo_estado='O') 
        #metodo_sql.MovimientoCajero(cod_cajero=3, nuevo_estado='F')  
        #metodo_sql.MovimientoCajero(cod_cajero=4, nuevo_estado='M') 
        metodo_sql.RealizarAuditoria( cod_mov_a=1, cod_cajero=3  )
        ConexionSQL.CerrarSQL()
#Prueba()
#phantonsita
import pyodbc
from tkinter import messagebox

server = "NESTORPC\\NESTOR"
database = "progra 3"
global conn 

class Conexion:
    # validar usuario activo / inactivo
    conn = None # variable global para la conexion
    def LoginSQL(usuario, contrasena):
        try:
            if usuario and contrasena:
                Conexion.conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={usuario};PWD={contrasena};TrustServerCertificate=yes;')
                print("conexion SQL exitosa", usuario)
                messagebox.showinfo("Tarea Programada 5", f'Login Exitoso {usuario}')
                return True
            else :
                messagebox.showwarning("Tarea Programada 5", 'Usuario / Contrasena Incorrecto')
                return False
        except pyodbc.Error as e:
            messagebox.showerror("Tarea Programada 5", 'Usuario / Contrasena Incorrecto. \n Intente de nuevo')
            return False
        # se validan las credenciales y si son validas se ingresa al programa y a la Base Datos. 

    def CerrarSQL():
        try:
            if Conexion.conn:
                Conexion.conn.close()
                print('Se realizo el cierre de la Conexion de BD')
                messagebox.showinfo("Tarea Programada 5", "Sesion cerrada correctamente")
                Conexion.conn = None
            else:
                messagebox.showinfo("Tarea Programada 5", "No hay conexión para cerrar")
        except pyodbc.Error as e:
            messagebox.showerror("Tarea Programada 5", f'Error al cerrar la conexión: {e}')
        # metodo para cerrar la Sesion de la Base de Datos

# fin class Conexion

class MetodosSQL:

    def ValidarUsuario():
        #Usuario max 35 char
        pass

    def LeerUsuariosSQL(conn): # uso el parametro gobal para ingresar a la BD y realizar la consulta
        # cursor = senala una accion en BD
        cursor = Conexion.conn.cursor()
        query = """ SELECT u.Codigo, u.Usuario, u.Nombre,r.Descripcion_rol, e.Descripcion_estado 
        FROM Usuarios u INNER JOIN Roles r ON u.Rol = r.Rol INNER JOIN Estados e ON u.Estado = e.Estado""" 

        """ INNER JOIN combina las tablas
        u/r/e son alias de las tablas
        INNER JOIN Roles r ON u.Rol = r.Rol =  indica como se combinan las filas coincidiendo los campos
        """
        cursor.execute(query) # Se ejecuta el Query

        ResConsulta = cursor.fetchall() # obtengo todas las filas de BD 
        nuevosDatos = []
        for consulta in ResConsulta:
            codigo = int (consulta[0])
            usuario = consulta[1].strip()
            nombre = consulta[2].strip()
            rol = consulta[3].strip()
            estado = consulta[4].strip()
            
            nuevosDatos.append((codigo, usuario, nombre,rol,estado))
            print(nuevosDatos)
        cursor.close() # se cierra la operacion
        return nuevosDatos
        
    def EscribirSQL(usuario, contrasena, nombre, rol, estado, CodigoMovimiento):
        try:
            cursor = Conexion.conn.cursor()
            queryUsuario = """ INSERT INTO Usuarios (Usuario, Contra, Nombre, Rol, Estado) VALUES (?,?,?,?,?) """
            cursor.execute(queryUsuario,usuario,contrasena,nombre,rol,estado)

            cursor.execute("SELECT @@IDENTITY AS id") # selecciono el codigo declarado como identity = unico y autosumable
            codigoUsuario = cursor.fetchone()[0] # obtengo el Identity

            queryAuditoria = """ INSERT INTO Auditoria (codigo_usuario, codigo_movimiento, fecha_hora) VALUES(?,?,GETDATE()) """
            #agrego los datos a la tabla Auditoria el valor GETDATE() da la fechahora 
            cursor.execute(queryAuditoria, codigoUsuario, CodigoMovimiento) 

            Conexion.conn.commit() # se aceptan los cambios 
            messagebox.showinfo("Tarea Programada 5", " Usuario Ingresado Correctamente")
            print("Tarea Programada 5", " Usuario Ingresado Correctamente")
            print(f"Usuario agregado: Codigo: {codigoUsuario}, Usuario: {usuario}, Contrasena: {contrasena}, Nombre: {nombre}, Rol: {rol}, Estado: {estado}")
            cursor.close() # cierro la operacion
        except pyodbc.Error as e:
            Conexion.conn.rollback() # si existe un error se rechaza la operacion
            print(messagebox.showerror("Tarea Programada 5", f" Error al Ingresar el Usuario  {e}"))
            
    def ActualizarSQL():
        pass
    def EliminarSQL():
        pass
# fin class Metodos SQL
#-------------------------------------------------------------------------------------------------#
def prueba():
    if Conexion.LoginSQL(usuario="Nestor1", contrasena="nestor"):
        MetodosSQL.LeerUsuariosSQL(Conexion.conn)
        MetodosSQL.EscribirSQL(Conexion.conn)
        Conexion.CerrarSQL()


#prueba()
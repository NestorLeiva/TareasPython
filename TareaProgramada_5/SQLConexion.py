import pyodbc
from tkinter import messagebox

server = "NESTORPC\\NESTOR"
database = "progra 3"
global conn  # variable global para la conexion

class Conexion:
    conn = None # se le asigna un valor vacio
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
    # Metodo para validar las credenciales y si son validas se ingresa al programa y a la Base Datos. 

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

    def Auditoria(codigoUsuario, CodigoMovimiento):
        cursor = Conexion.conn.cursor()
        queryAuditoria = """INSERT INTO Auditoria (codigo_usuario, codigo_movimiento, fecha_hora) VALUES (?, ?, GETDATE())"""
        cursor.execute(queryAuditoria, codigoUsuario, CodigoMovimiento)
        Conexion.conn.commit()
        print(f"Auditoria = {codigoUsuario}, codigo_movimiento = {CodigoMovimiento}")
        cursor.close()
    # Metodo para realizar el Insert en la Tabla Auditoria  BD

    def LeerUsuariosSQL(conn): # uso el parametro gobal para ingresar a la BD y realizar la consulta
        # cursor = senala una accion en BD
        cursor = Conexion.conn.cursor()
        query = """ SELECT u.Codigo, u.Usuario, u.Contra, u.Nombre,r.Descripcion_rol, e.Descripcion_estado 
        FROM Usuarios u INNER JOIN Roles r ON u.Rol = r.Rol INNER JOIN Estados e ON u.Estado = e.Estado""" 

        """ INNER JOIN = combina las tablas
        u/r/e = son alias de las tablas
        INNER JOIN Roles r ON u.Rol = r.Rol = indica como se combinan las filas coincidiendo los campos"""
        cursor.execute(query) # Se ejecuta el Query

        ResConsulta = cursor.fetchall() # obtengo todas las filas de BD 
        nuevosDatos = []
        for consulta in ResConsulta:
            codigo = int (consulta[0])
            usuario = consulta[1].strip()
            contra = consulta[2].strip()
            nombre = consulta[3].strip()
            rol = consulta[4].strip()
            estado = consulta[5].strip()
            
            nuevosDatos.append((codigo,usuario,contra, nombre,rol,estado)) # agrego los datos 
            print(nuevosDatos)
        return nuevosDatos 
    # Metodo para realizar la lectura de las Tablas de BD
     
    def EscribirSQL(codigo,usuario,contrasena, nombre,rol,estado,CodigoMovimiento):
        try:
            cursor = Conexion.conn.cursor()
            queryUsuario = """ INSERT INTO Usuarios (Codigo, Usuario, Contra, Nombre, Rol, Estado) VALUES (?,?,?,?,?,?) """
            cursor.execute(queryUsuario,codigo,usuario,contrasena,nombre,rol,estado)

            MetodosSQL.Auditoria(codigo,CodigoMovimiento)

            Conexion.conn.commit() # se aceptan los cambios 
            messagebox.showinfo("Tarea Programada 5", " Usuario Ingresado Correctamente")
            print("Tarea Programada 5", " Usuario Ingresado Correctamente")
            print(f"Usuario agregado: Codigo: {codigo}, Usuario: {usuario}, Contrasena: {contrasena}, Nombre: {nombre}, Rol: {rol}, Estado: {estado}")
            Conexion.conn.close() # cierro la operacion
        except pyodbc.Error as e:
            Conexion.conn.rollback() # si existe un error se rechaza la operacion
            print(messagebox.showerror("Tarea Programada 5", f" Error al Ingresar el Usuario  {e}"))
    # Metodo para realizar el Insert en la BD
    
    def ConsultaSQL(codigo):
        try:
            cursor = Conexion.conn.cursor()
            queryConsulta = """SELECT u.Codigo, u.Usuario, u.Contra, u.Nombre, r.Descripcion_rol, e.Descripcion_estado 
            FROM Usuarios u INNER JOIN Roles r ON u.Rol = r.Rol INNER JOIN Estados e ON u.Estado = e.Estado WHERE Codigo = ?"""
            Qconsulta =  cursor.execute(queryConsulta, codigo)
            
            datos = []
            for consulta in Qconsulta.fetchall():
                cod = int(consulta[0])
                usuario = consulta[1].strip()
                contra = consulta[2].strip()
                nombre = consulta[3].strip()
                rol = consulta[4].strip()
                estado = consulta[5].strip()
                datos.append((cod,usuario, contra,nombre,rol,estado)) # se crea una tupla
                print('Consulta ',datos)
                return datos
        except pyodbc.Error as e:
            messagebox.showerror("Tarea Programada 5", "Error al realizar la Consutla \n Verifique los datos")
            print(f"Error al realizar la Consutla Verifique los datos {e}")
    # Metodo para realizar la consulta de un usuario 

    def ModificarSQL():
        
        pass
    def EliminarSQL():
        pass
# fin class Metodos SQL
#-------------------------------------------------------------------------------------------------#
def prueba():
    if Conexion.LoginSQL(usuario="Nestor1", contrasena="nestor"):
        #MetodosSQL.ModificarSQL(Conexion.conn, codigo=5)
        MetodosSQL.ConsultaSQL(codigo=2)
        Conexion.CerrarSQL()
#prueba()
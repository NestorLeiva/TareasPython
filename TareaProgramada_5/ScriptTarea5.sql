/*	Login: Nestor1	Password: nestor
	Login: Arlyn1	Password: arlyn
	*** Ejecutar el Query por Secciones ****
*/
USE [master]
GO
CREATE DATABASE [Progra 3]
USE [Progra 3]
/*----------------------------------------------------*/
-- Crear los logins si no existen
IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = N'Nestor1')
BEGIN
    CREATE LOGIN [Nestor1] WITH PASSWORD = N'nestor';
END
GO
IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = N'Arlyn1')
BEGIN
    CREATE LOGIN [Arlin1] WITH PASSWORD = N'arlyn';
END
GO
/*----------------------------------------------------*/
-- Crear usuarios
CREATE USER [Nestor_1] FOR LOGIN [Nestor1] WITH DEFAULT_SCHEMA=[dbo]
GO
CREATE USER [Arlin_1] FOR LOGIN [Arlin1] WITH DEFAULT_SCHEMA=[dbo]
GO
/*----------------------------------------------------*/
-- Asignar roles a los usuarios
ALTER ROLE [db_owner] ADD MEMBER [Nestor_1]
GO
ALTER ROLE [db_owner] ADD MEMBER [Arlin_1]
GO
/*----------------------------------------------------*/
CREATE TABLE [dbo].[Usuarios](
	[Codigo] [numeric](18, 0) IDENTITY(1,1) NOT NULL PRIMARY KEY,
	[Usuario] [nchar](35) NOT NULL,
	[Contra] [nchar](10) NOT NULL,
	[Nombre] [nchar](35) NOT NULL,
	[Rol] [numeric](1, 0) NOT NULL,
	[Estado] [numeric](1, 0) NOT NULL)

/*----------------------------------------------------*/
CREATE TABLE [dbo].[Roles](
	[Rol] [numeric](1, 0) NOT NULL PRIMARY KEY,
	[Descripcion_rol] [nchar](10) NOT NULL)

/*----------------------------------------------------*/
CREATE TABLE [dbo].[Estados](
	[Estado] [numeric](1, 0) NOT NULL PRIMARY KEY,
	[Descripcion_estado] [nchar](10) NOT NULL)

/*----------------------------------------------------*/
CREATE TABLE [dbo].[Auditoria](
	[codigo_usuario]      numeric (18,0)   not null PRIMARY KEY,
	[codigo_movimiento]   numeric (5,0)   not null, 
	[fecha_hora]          datetime        not null ) /*fecha del moviento*/
	/*  codigo de usuario = usuario tabla usuario
        codigo mov = tabla desc.mov codigo_mov
        fecha_hora = del dia de la modificiacion
     */
/*----------------------------------------------------*/
CREATE TABLE [dbo].[Desc_Mov_Auditoria](
	[codigo_movimiento]   numeric (5,0)  not null PRIMARY KEY,
	[descripcion_movimiento] nvarchar(50) not null)

INSERT INTO Usuarios (Codigo, Usuario, Contra, Nombre, Rol, Estado) VALUES(1, 'Arlyn', 'arlyn', 'Arlyn Madriz',1,1);
INSERT INTO Usuarios (Codigo, Usuario, Contra, Nombre, Rol, Estado) VALUES(2, 'Nestor', 'nestor','Nestor Leiva',2,1);
INSERT INTO Roles(Rol, Descripcion_rol) VALUES(1, 'Admin');
INSERT INTO Roles(Rol, Descripcion_rol) VALUES(2, 'Conta');
INSERT INTO Roles (Rol, Descripcion_rol) VALUES(3,'Supervisor');
INSERT INTO Roles (Rol, Descripcion_rol) VALUES(4, 'Operario');
INSERT INTO Estados(Estado, Descripcion_estado) VALUES(1, 'Activo');
INSERT INTO Estados (Estado, Descripcion_estado) VALUES(2, 'InActivo');
INSERT INTO Desc_Mov_Auditoria (codigo_movimiento, descripcion_movimiento) VALUES(1, 'Inserto Nuevo Registro');
INSERT INTO Desc_Mov_Auditoria (codigo_movimiento, descripcion_movimiento) VALUES(2, 'Modifico Nuevo Registro');
INSERT INTO Desc_Mov_Auditoria (codigo_movimiento, descripcion_movimiento) VALUES(3, 'Elimino Registro');
INSERT INTO Desc_Mov_Auditoria (codigo_movimiento, descripcion_movimiento) VALUES(4, 'Consulta Registro');	
/*----------------------------------------------------*/
ALTER TABLE [dbo].[Usuarios]  WITH CHECK ADD  CONSTRAINT [FK_Usuarios_Estados] FOREIGN KEY([Estado])
REFERENCES [dbo].[Estados] ([Estado])
GO
ALTER TABLE [dbo].[Usuarios] CHECK CONSTRAINT [FK_Usuarios_Estados]
GO
ALTER TABLE [dbo].[Usuarios]  WITH CHECK ADD  CONSTRAINT [FK_Usuarios_Roles] FOREIGN KEY([Rol])
REFERENCES [dbo].[Roles] ([Rol])
GO
ALTER TABLE [dbo].[Usuarios] CHECK CONSTRAINT [FK_Usuarios_Roles]
GO
/*-----------------------------------------------------------*/

-- Crear relaciones
ALTER TABLE [dbo].[Usuarios]  WITH CHECK ADD  CONSTRAINT [FK_Usuarios_Estados] FOREIGN KEY([Estado])
REFERENCES [dbo].[Estados] ([Estado])
GO
ALTER TABLE [dbo].[Usuarios] CHECK CONSTRAINT [FK_Usuarios_Estados]
GO
ALTER TABLE [dbo].[Usuarios]  WITH CHECK ADD  CONSTRAINT [FK_Usuarios_Roles] FOREIGN KEY([Rol])
REFERENCES [dbo].[Roles] ([Rol])
GO
ALTER TABLE [dbo].[Usuarios] CHECK CONSTRAINT [FK_Usuarios_Roles]
GO
ALTER TABLE [dbo].[Auditoria]  WITH CHECK ADD  CONSTRAINT [FK_Auditoria_Desc_Mov_Auditoria1] FOREIGN KEY([codigo_movimiento])
REFERENCES [dbo].[Desc_Mov_Auditoria] ([codigo_movimiento])
GO
ALTER TABLE [dbo].[Auditoria] CHECK CONSTRAINT [FK_Auditoria_Desc_Mov_Auditoria1]
GO
ALTER TABLE [dbo].[Auditoria]  WITH CHECK ADD  CONSTRAINT [FK_Auditoria_Usuarios] FOREIGN KEY([codigo_usuario])
REFERENCES [dbo].[Usuarios] ([Codigo])
GO
ALTER TABLE [dbo].[Auditoria] CHECK CONSTRAINT [FK_Auditoria_Usuarios]
GO
USE [master]
GO
ALTER DATABASE [Progra 3] SET  READ_WRITE 
GO
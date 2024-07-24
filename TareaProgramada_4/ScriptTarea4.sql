/*
   miércoles, 24 de julio de 202412:13:40
   User: 
   Server: NESTORPC\NESTOR
   Database: progra3
   Application: 
*/

/* To prevent any potential data loss issues, you should review this script in detail before running it outside the context of the database designer.*/
BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
ALTER TABLE dbo.Usuarios
	DROP CONSTRAINT FK_Usuarios_Estados
GO
ALTER TABLE dbo.Estados SET (LOCK_ESCALATION = TABLE)
GO
COMMIT
select Has_Perms_By_Name(N'dbo.Estados', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.Estados', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.Estados', 'Object', 'CONTROL') as Contr_Per BEGIN TRANSACTION
GO
ALTER TABLE dbo.Usuarios
	DROP CONSTRAINT FK_Usuarios_Roles
GO
ALTER TABLE dbo.Roles SET (LOCK_ESCALATION = TABLE)
GO
COMMIT
select Has_Perms_By_Name(N'dbo.Roles', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.Roles', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.Roles', 'Object', 'CONTROL') as Contr_Per BEGIN TRANSACTION
GO
CREATE TABLE dbo.Tmp_Usuarios
	(
	Codigo numeric(18, 0) NOT NULL,
	Usuario nchar(10) NOT NULL,
	Contra nchar(10) NOT NULL,
	Nombre nchar(20) NOT NULL,
	Rol numeric(1, 0) NOT NULL,
	Estado numeric(1, 0) NOT NULL
	)  ON [PRIMARY]
GO
ALTER TABLE dbo.Tmp_Usuarios SET (LOCK_ESCALATION = TABLE)
GO
IF EXISTS(SELECT * FROM dbo.Usuarios)
	 EXEC('INSERT INTO dbo.Tmp_Usuarios (Codigo, Usuario, Contra, Nombre, Rol, Estado)
		SELECT Codigo, Usuario, Contra, Nombre, Rol, Estado FROM dbo.Usuarios WITH (HOLDLOCK TABLOCKX)')
GO
DROP TABLE dbo.Usuarios
GO
EXECUTE sp_rename N'dbo.Tmp_Usuarios', N'Usuarios', 'OBJECT' 
GO
ALTER TABLE dbo.Usuarios ADD CONSTRAINT
	PK_Usuarios PRIMARY KEY CLUSTERED 
	(
	Codigo,
	Usuario
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO
ALTER TABLE dbo.Usuarios ADD CONSTRAINT
	FK_Usuarios_Roles FOREIGN KEY
	(
	Rol
	) REFERENCES dbo.Roles
	(
	Rol
	) ON UPDATE  NO ACTION 
	 ON DELETE  NO ACTION 
	
GO
ALTER TABLE dbo.Usuarios ADD CONSTRAINT
	FK_Usuarios_Estados FOREIGN KEY
	(
	Estado
	) REFERENCES dbo.Estados
	(
	Estados
	) ON UPDATE  NO ACTION 
	 ON DELETE  NO ACTION 
	
GO
COMMIT
select Has_Perms_By_Name(N'dbo.Usuarios', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.Usuarios', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.Usuarios', 'Object', 'CONTROL') as Contr_Per 
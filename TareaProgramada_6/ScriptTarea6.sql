USE [Progra3Cajero]


SELECT * FROM sys.server_principals WHERE name = '*usuario*';    -- valido que exista el usuario
GO

/****** Object:  User [NestorCA]    Script Date: 14/8/2024 22:23:29 ******/
CREATE LOGIN [NestorCA] WITH PASSWORD = 'nestor_10';            -- se crea el login con la contrasena
GO
CREATE USER [NestorCA] FOR LOGIN [NestorCA] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [NestorCA] 
GO
/*Password = nestor10*/
/****** Object:  User [ArlynCA]    Script Date: 20/8/2024 10:38:58 ******/
CREATE LOGIN [ArlynCA] WITH PASSWORD = 'arlyn_10';            -- se crea el login con la contrasena
GO
CREATE USER [ArlynCA] FOR LOGIN [ArlynCA] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [ArlynCA];
GO
/*Password = arlyn10*/
/****** Object:  User [MarlonCA]    Script Date: 20/8/2024 10:38:58 ******/
CREATE LOGIN [MarlonCA] WITH PASSWORD = 'marlon_10';            -- se crea el login con la contrasena
GO
CREATE USER [MarlonCA] FOR LOGIN [MarlonCA] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [MarlonCA];
GO
/*Password = marlon10*/
/****** Object:  User [SamuelCA]    Script Date: 20/8/2024 10:38:58 ******/

CREATE LOGIN [SamuelCA] WITH PASSWORD = 'samuel_10';            -- se crea el login con la contrasena
Go
CREATE USER [SamuelCA] FOR LOGIN [SamuelCA] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [SamuelCA];
GO
/*Password = samuel10*/
/****** Object:  Table [dbo].[Auditoria]    Script Date: 14/8/2024 22:23:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Auditoria](
	[cod_usuario_a] [numeric](1, 0) NOT NULL,
	[movimiento_a] [numeric](1, 0) NOT NULL,
	[fecha_mov_a] [datetime] NOT NULL,
	[cod_cajero_a] [numeric](1, 0) NOT NULL,
 CONSTRAINT [PK_Auditoria_1] PRIMARY KEY CLUSTERED 
(
	[cod_usuario_a] ASC,
	[movimiento_a] ASC,
	[fecha_mov_a] ASC,
	[cod_cajero_a] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cajero]    Script Date: 14/8/2024 22:23:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cajero](
	[cod_cajero] [numeric](1, 0) NOT NULL,
	[ubicacion] [nvarchar](50) NOT NULL,
	[estado] [nvarchar](1) NOT NULL,
 CONSTRAINT [PK_Cajero] PRIMARY KEY CLUSTERED 
(
	[cod_cajero] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cuenta]    Script Date: 14/8/2024 22:23:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cuenta](
	[cod_usuario_c] [numeric](1, 0) NOT NULL,
	[numero_cuenta_c] [numeric](18, 0) NOT NULL,
	[saldo_c] [numeric](18, 0) NOT NULL,
	[movimiento_c] [numeric](1, 0) NOT NULL,
 CONSTRAINT [PK_Cuenta] PRIMARY KEY CLUSTERED 
(
	[cod_usuario_c] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Movimiento]    Script Date: 14/8/2024 22:23:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Movimiento](
	[movimiento_m] [numeric](1, 0) NOT NULL,
	[descripcion_m] [nvarchar](10) NOT NULL,
 CONSTRAINT [PK_Movimiento] PRIMARY KEY CLUSTERED 
(
	[movimiento_m] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Usuario]    Script Date: 14/8/2024 22:23:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Usuario](
	[cod_usuario] [numeric](1, 0) NOT NULL,
	[usuario] [nvarchar](20) NOT NULL,
	[contra] [nvarchar](10) NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[estado] [numeric](1, 0) NOT NULL,
 CONSTRAINT [PK_Usuario] PRIMARY KEY CLUSTERED 
(
	[cod_usuario] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Auditoria]  WITH CHECK ADD  CONSTRAINT [FK_Auditoria_Cajero] FOREIGN KEY([cod_cajero_a])
REFERENCES [dbo].[Cajero] ([cod_cajero])
GO
ALTER TABLE [dbo].[Auditoria] CHECK CONSTRAINT [FK_Auditoria_Cajero]
GO
ALTER TABLE [dbo].[Auditoria]  WITH CHECK ADD  CONSTRAINT [FK_Auditoria_Movimiento] FOREIGN KEY([movimiento_a])
REFERENCES [dbo].[Movimiento] ([movimiento_m])
GO
ALTER TABLE [dbo].[Auditoria] CHECK CONSTRAINT [FK_Auditoria_Movimiento]
GO
ALTER TABLE [dbo].[Auditoria]  WITH CHECK ADD  CONSTRAINT [FK_Auditoria_Usuario] FOREIGN KEY([cod_usuario_a])
REFERENCES [dbo].[Usuario] ([cod_usuario])
GO
ALTER TABLE [dbo].[Auditoria] CHECK CONSTRAINT [FK_Auditoria_Usuario]
GO
ALTER TABLE [dbo].[Usuario]  WITH CHECK ADD  CONSTRAINT [FK_Usuario_Cuenta] FOREIGN KEY([cod_usuario])
REFERENCES [dbo].[Cuenta] ([cod_usuario_c])
GO
ALTER TABLE [dbo].[Usuario] CHECK CONSTRAINT [FK_Usuario_Cuenta]
GO
/*-----------------------------------------------------------------------------------------------------------*/

INSERT INTO Usuarios (Cod_Usuario, Usuario , Contra, Nombre, Estado) VALUES (1, 'ArlynCA','arlyn10', 'Arlyn Madriz', 1);
INSERT INTO Usuarios (Cod_Usuario, Usuario , Contra, Nombre, Estado) VALUES (2, 'NestorCA','nestor10', 'Nestor Leiva', 1);
INSERT INTO Usuarios (Cod_Usuario, Usuario , Contra, Nombre, Estado) VALUES (3, 'SamuelCA','samuel10', 'Samuel Barahona', 1);
INSERT INTO Usuarios (Cod_Usuario, Usuario , Contra, Nombre, Estado) VALUES (4, 'MarlonCA','Marlon10', 'Marlon Matamoros', 1);

INSERT INTO Cuentas (cod_usuario_c, numero_cuenta_c , Saldo_c, Movimiento_c) VALUES (1, 10,5000, 1);
INSERT INTO Cuentas (cod_usuario_c, numero_cuenta_c , Saldo_c, Movimiento_c) VALUES (2, 10,5000, 1);
INSERT INTO Cuentas (cod_usuario_c, numero_cuenta_c , Saldo_c, Movimiento_c) VALUES (3, 10,5000, 1);
INSERT INTO Cuentas (cod_usuario_c, numero_cuenta_c , Saldo_c, Movimiento_c) VALUES (4, 10,5000, 1);

INSERT INTO Cajeros (cod_cajero, Ubicacion, Estado) VALUES (1,'Cartago','L')
INSERT INTO Cajeros (cod_cajero, Ubicacion, Estado) VALUES (2,'Heredia','A')
INSERT INTO Cajeros (cod_cajero, Ubicacion, Estado) VALUES (3,'San Jose','O')
INSERT INTO Cajeros (cod_cajero, Ubicacion, Estado) VALUES (3,'San Jose','M')

INSERT INTO Movimientos (Movimiento_m, Descripcion_m) VALUES (1,'Deposito')
INSERT INTO Movimientos (Movimiento_m, Descripcion_m) VALUES (2,'Retiro')
INSERT INTO Movimientos (Movimiento_m, Descripcion_m) VALUES (3,'Consulta')
INSERT INTO Movimientos (Movimiento_m, Descripcion_m) VALUES (4,'CambioEsta')

INSERT INTO Auditoria (cod_usuario_a, movimiento_a, fecha_mov_a, cod_cajero_a) VALUES (1, 1, GETDATE(), 1)
INSERT INTO Auditoria (cod_usuario_a, movimiento_a, fecha_mov_a, cod_cajero_a) VALUES (2, 2, GETDATE(), 2)
INSERT INTO Auditoria (cod_usuario_a, movimiento_a, fecha_mov_a, cod_cajero_a) VALUES (3, 3, GETDATE(), 3)
INSERT INTO Auditoria (cod_usuario_a, movimiento_a, fecha_mov_a, cod_cajero_a) VALUES (4, 4, GETDATE(), 1)


SELECT * FROM Usuario
SELECT * FROM Cuenta;
SELECT * FROM Cajero;
SELECT * FROM Auditoria;
SELECT * FROM Movimiento;

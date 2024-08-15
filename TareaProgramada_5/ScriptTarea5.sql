/*	Login: Nestor1	Password: nestor
	Login: Arlyn1	Password: arlyn
*/
USE [Progra 3]
GO
/****** Object:  User [Arlin_1]    Script Date: 14/8/2024 22:28:34 ******/
CREATE USER [Arlin_1] FOR LOGIN [Arlin1] WITH DEFAULT_SCHEMA=[dbo]
GO
/****** Object:  User [Nestor_1]    Script Date: 14/8/2024 22:28:34 ******/
CREATE USER [Nestor_1] FOR LOGIN [Nestor1] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [Arlin_1]
GO
ALTER ROLE [db_owner] ADD MEMBER [Nestor_1]
GO

-- Conceder permisos y agregar al rol securityadmin
GRANT ALTER ANY LOGIN TO Nestor1;
ALTER SERVER ROLE securityadmin ADD MEMBER Nestor1;
GO
-- Conceder permisos y agregar al rol securityadmin
GRANT ALTER ANY LOGIN TO Arlin_1;
ALTER SERVER ROLE securityadmin ADD MEMBER Arlin_1;
GO

/****** Object:  Table [dbo].[Auditoria]    Script Date: 14/8/2024 22:28:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Auditoria](
	[codigo_usuario] [numeric](18, 0) NOT NULL,
	[codigo_movimiento] [numeric](5, 0) NOT NULL,
	[fecha_hora] [datetime] NOT NULL,
 CONSTRAINT [PK__Auditori__37F064A0F6E9FBC7] PRIMARY KEY CLUSTERED 
(
	[codigo_usuario] ASC,
	[codigo_movimiento] ASC,
	[fecha_hora] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Desc_Mov_Auditoria]    Script Date: 14/8/2024 22:28:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Desc_Mov_Auditoria](
	[codigo_movimiento] [numeric](5, 0) NOT NULL,
	[descripcion_movimiento] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo_movimiento] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Estados]    Script Date: 14/8/2024 22:28:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Estados](
	[Estado] [numeric](1, 0) NOT NULL,
	[Descripcion_estado] [nchar](10) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Estado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Roles]    Script Date: 14/8/2024 22:28:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Roles](
	[Rol] [numeric](1, 0) NOT NULL,
	[Descripcion_rol] [nchar](10) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Rol] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Usuarios]    Script Date: 14/8/2024 22:28:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Usuarios](
	[Codigo] [numeric](18, 0) NOT NULL,
	[Usuario] [nchar](35) NOT NULL,
	[Contra] [nchar](10) NOT NULL,
	[Nombre] [nchar](35) NOT NULL,
	[Rol] [numeric](1, 0) NOT NULL,
	[Estado] [numeric](1, 0) NOT NULL,
 CONSTRAINT [PK__Usuarios__06370DAD03DF8F87] PRIMARY KEY CLUSTERED 
(
	[Codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
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

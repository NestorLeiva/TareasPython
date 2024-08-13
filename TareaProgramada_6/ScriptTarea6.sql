USE [Progra3Cajero]
GO
/****** Object:  User [NestorC]    Script Date: 12/8/2024 22:50:23 ******/
CREATE USER [NestorC] FOR LOGIN [NestorC] WITH DEFAULT_SCHEMA=[dbo]
/* usuario="NestorC", contrasena="nestor10"*/
GO
/****** Object:  Table [dbo].[Auditoria]    Script Date: 12/8/2024 22:50:23 ******/
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
	[cod_usuario_a] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cajero]    Script Date: 12/8/2024 22:50:23 ******/
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
/****** Object:  Table [dbo].[Cuenta]    Script Date: 12/8/2024 22:50:23 ******/
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
/****** Object:  Table [dbo].[Movimiento]    Script Date: 12/8/2024 22:50:23 ******/
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
/****** Object:  Table [dbo].[Usuario]    Script Date: 12/8/2024 22:50:23 ******/
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
	[usuario] ASC
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
ALTER TABLE [dbo].[Usuario]  WITH CHECK ADD  CONSTRAINT [FK_Usuario_Auditoria] FOREIGN KEY([cod_usuario])
REFERENCES [dbo].[Auditoria] ([cod_usuario_a])
GO
ALTER TABLE [dbo].[Usuario] CHECK CONSTRAINT [FK_Usuario_Auditoria]
GO
ALTER TABLE [dbo].[Usuario]  WITH CHECK ADD  CONSTRAINT [FK_Usuario_Cuenta] FOREIGN KEY([cod_usuario])
REFERENCES [dbo].[Cuenta] ([cod_usuario_c])
GO
ALTER TABLE [dbo].[Usuario] CHECK CONSTRAINT [FK_Usuario_Cuenta]
GO

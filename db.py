import psycopg2
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20))
    tipo_documento = db.Column(db.String(50), default='DNI')
    documento = db.Column(db.String(20))
    estado = db.Column(db.String(20), default='Activo')
   
class Producto(db.Model):
    __tablename__ = 'producto' 
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(150), nullable=False) 
    precio = db.Column(db.Numeric(10, 2), nullable=False) 
    descripcion = db.Column(db.Text, nullable=True)    
    imagen = db.Column(db.String(255), nullable=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria_producto.id')) 

class CategoriaProducto(db.Model):
    __tablename__ = 'categoria_producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(20), default='Activo')

    # Relación con la tabla Producto
    productos = db.relationship('Producto', backref='categoria', lazy=True)


class HistorialPagos(db.Model):
    __tablename__ = 'historial_pagos'
    id = db.Column(db.Integer, primary_key=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id', ondelete='CASCADE'), nullable=False)
    monto = db.Column(db.Numeric(10, 2), nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    referencia_voucher = db.Column(db.String(255))


class DetallePedido(db.Model):
    __tablename__ = 'detalle_pedido'
    id = db.Column(db.Integer, primary_key=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id', ondelete='CASCADE'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    especificaciones = db.Column(db.Text)
    archivo_diseno = db.Column(db.String(255))  

def get_connection(): 
    
    URI_SUPABASE = "postgresql://postgres.byixvuagnonvxjhhsnkn:SCARFSKYLA21@aws-1-us-west-2.pooler.supabase.com:6543/postgres"
    
    return psycopg2.connect(URI_SUPABASE)
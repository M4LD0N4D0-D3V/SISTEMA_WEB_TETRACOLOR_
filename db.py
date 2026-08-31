import psycopg2
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario' 
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(255), nullable=False)        
    documento = db.Column(db.String(11), unique=True, nullable=True) # DNI o RUC
    telefono = db.Column(db.String(20), nullable=True) 
   
class Producto(db.Model):
    __tablename__ = 'producto' 
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(150), nullable=False) 
    precio = db.Column(db.Numeric(10, 2), nullable=False) 
    descripcion = db.Column(db.Text, nullable=True)    
    imagen = db.Column(db.String(255), nullable=True)   

def get_connection(): 
    
    URI_SUPABASE = "postgresql://postgres.byixvuagnonvxjhhsnkn:SCARFSKYLA21@aws-1-us-west-2.pooler.supabase.com:6543/postgres"
    
    return psycopg2.connect(URI_SUPABASE)
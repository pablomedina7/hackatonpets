from flask_sqlalchemy import SQLAlchemy

# Crear el objeto db
db = SQLAlchemy()

# Definir el modelo 'Mascota'
class Mascota(db.Model):
    __tablename__ = 'mascotas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    fecha_adopcion = db.Column(db.DateTime, default=db.func.current_timestamp())

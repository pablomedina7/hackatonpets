from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Alimentacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mascota_id = db.Column(db.Integer, nullable=False)  # Asociado a la mascota
    fecha_alimentacion = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Alimentacion mascota_id={self.mascota_id} fecha={self.fecha_alimentacion}>"

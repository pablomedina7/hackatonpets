from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alimentacion(db.Model):
    __tablename__ = 'alimentacion'

    id = db.Column(db.Integer, primary_key=True)
    mascota_id = db.Column(db.Integer, nullable=False)
    fecha_alimentacion = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Alimentacion {self.mascota_id}>'

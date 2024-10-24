from models.alimentationdb_model import db, Alimentacion
from datetime import datetime

def registrar_alimentacion(mascota_id):
    nueva_alimentacion = Alimentacion(
        mascota_id=mascota_id,
        fecha_alimentacion=datetime.now()
    )
    db.session.add(nueva_alimentacion)
    db.session.commit()
    return f"La mascota con ID {mascota_id} ha sido alimentada."

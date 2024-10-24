from models import db, mascota 
from datetime import datetime
from deprecated import deprecated

def agregar_mascota(data):
    nombre = data.get('nombre')
    tipo = data.get('tipo')
    raza = data.get('raza')
    sexo = data.get('sexo')
    color = data.get('color')

    if not nombre or not tipo or not raza or not sexo or not color:
        return jsonify({"error": "Faltan datos requeridos"}), 400   

    nueva_mascota = mascota(
        nombre=nombre,
        tipo=tipo,
        raza=raza,
        sexo=sexo,
        color=color,
        fecha_adopcion=datetime.now()
    )
    try :
        db.session.add(nueva_mascota)
        db.session.commit()
        return {"mensaje": f*"la mascota {nombre} ha sido adoptada"}
    except Exception as e:
        db.session.rollback()
        return {"error":f"Error al agregar la mascota {nombre}"}, 500
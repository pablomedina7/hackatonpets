from flask import Blueprint, request, jsonify
from models import db, Alimentacion
import datetime


# Creamos el blueprint para las rutas
alimentos_bp = Blueprint('alimentos_bp', __name__)

@alimentos_bp.route('/alimento', methods=['POST'])
@alimentos_bp.route('/alimento', methods=['POST'])
def alimento_mascota():
    data = request.get_json()
    mascota_id = data['mascotaId']

    # Verificar si la mascota ha sido adoptada
    conn = sqlite3.connect("adopcion.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM adopcion WHERE mascota_id = ?', (mascota_id,))
    adopcion = cursor.fetchone()
    conn.close()

    if not adopcion:
        return jsonify({"mensaje": "La mascota no ha sido adoptada y no puede ser alimentada."}), 400

    # Si la mascota ha sido adoptada, registrar la alimentación
    hora_alimentacion = datetime.datetime.now().isoformat()
    nueva_alimentacion = Alimentacion(mascota_id=mascota_id, hora_alimentacion=hora_alimentacion)
    
    db.session.add(nueva_alimentacion)
    db.session.commit()

    return jsonify({
        "mensaje": "Mascota alimentada",
        "alimentacion": {
            'mascotaId': mascota_id,
            'hora_alimentacion': hora_alimentacion
        }
    }), 201

@alimentos_bp.route('/ultima_alimentacion/<int:mascota_id>', methods = ['GET'])
def obtener_ultima_alimentacion(mascota_id):
    # Obtener la última vez que la mascota fue alimentada
    ultima_alimentacion = Alimentacion.query.filter_by(mascota_id = mascota_id).order_by(Alimentacion.id.desc()).first()
    if ultima_alimentacion:
        return({
            'mascotaId' : ultima_alimentacion.mascota_id,
            'hora_alimentacion' : ultima_alimentacion.hora_alimentacion
        })
    else:
        return jsonify({"mensaje": "Mascota no ha sido alimentada aun "}), 404
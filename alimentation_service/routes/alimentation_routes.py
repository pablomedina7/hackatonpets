from flask import Blueprint, request, jsonify
from models.alimentationdb_model import db, Alimentacion

alimentacion_bp = Blueprint('alimentacion', __name__)

@alimentacion_bp.route('/alimentar', methods=['POST'])
def alimentar_mascota():
    data = request.get_json()
    mascota_id = data.get('mascota_id')

    if not mascota_id:
        return jsonify({"error": "ID de la mascota es requerido"}), 400

    nueva_alimentacion = Alimentacion(mascota_id=mascota_id)
    db.session.add(nueva_alimentacion)
    db.session.commit()

    return jsonify({"message": f"La mascota {mascota_id} ha sido alimentada.", "fecha_alimentacion": nueva_alimentacion.fecha_alimentacion}), 201

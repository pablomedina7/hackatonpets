from flask import Blueprint, request, jsonify
from models.alimentationdb_model import db, Alimentacion
from datetime import datetime

alimentacion_bp = Blueprint('alimentacion', __name__)

@alimentacion_bp.route('/alimentar', methods=['POST'])
def alimentar_mascota():
    data = request.json
    mascota_id = data.get('mascota_id')
    
    if not mascota_id:
        return jsonify({"error": "El ID de la mascota es obligatorio."}), 400
    
    nueva_alimentacion = Alimentacion(
        mascota_id=mascota_id,
        fecha_alimentacion=datetime.now()
    )
    
    try:
        db.session.add(nueva_alimentacion)
        db.session.commit()
        return jsonify({"mensaje": f"La mascota con ID {mascota_id} ha sido alimentada."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error al alimentar la mascota: {str(e)}"}), 500

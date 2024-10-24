from flask import Blueprint, request, jsonify
from models.adoptionbd_model import db, Mascota

adopcion_bp = Blueprint('adopcion', __name__)

@adopcion_bp.route('/adoptar', methods=['POST'])
def adoptar_mascota():
    data = request.get_json()
    nombre = data.get('nombre')
    tipo = data.get('tipo')

    if not nombre or not tipo:
        return jsonify({"error": "Nombre y tipo de mascota son requeridos"}), 400

    nueva_mascota = Mascota(nombre=nombre, tipo=tipo)
    db.session.add(nueva_mascota)
    db.session.commit()

    return jsonify({"message": f"{nombre} ha sido adoptado.", "petId": nueva_mascota.id}), 201

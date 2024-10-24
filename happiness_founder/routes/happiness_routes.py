from flask import Blueprint, jsonify
import requests

happiness_bp = Blueprint('happiness', __name__)

@happiness_bp.route('/felicidad/<int:mascota_id>', methods=['GET'])
def obtener_felicidad(mascota_id):
    response = requests.get(f'http://localhost:5002/alimentar/{mascota_id}')
    
    if response.status_code != 200:
        return jsonify({"error": "No se pudo obtener la información de alimentación."}), 500

    fecha_alimentacion = response.json().get('fecha_alimentacion')

    # Aquí puedes agregar la lógica para calcular la felicidad en función de la fecha de alimentación
    return jsonify({"felicidad": "Feliz" if fecha_alimentacion else "Triste"})

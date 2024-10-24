from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de adopción
@app.route('/adopcion', methods=['GET', 'POST'])
def adopcion():
    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre')
        tipo = data.get('tipo')
        # Enviar datos al microservicio de adopción
        response = requests.post('http://localhost:5001/adoptar', json={'nombre': nombre, 'tipo': tipo})
        if response.status_code == 201:
            return jsonify({"message": f"{nombre} ha sido adoptado con éxito."})
        else:
            return jsonify({"error": "Error al adoptar la mascota"}), 500
    return render_template('adopcion.html')

# Ruta para la página de alimentar
@app.route('/alimentar', methods=['GET', 'POST'])
def alimentar():
    if request.method == 'POST':
        data = request.get_json()
        mascota_id = data.get('mascota_id')
        # Enviar datos al microservicio de alimentación
        response = requests.post('http://localhost:5002/alimentar', json={'mascota_id': mascota_id})
        if response.status_code == 201:
            return jsonify({"message": f"La mascota {mascota_id} ha sido alimentada con éxito."})
        else:
            return jsonify({"error": "Error al alimentar la mascota"}), 500
    return render_template('alimentar.html')

# Ruta para la página de felicidad
@app.route('/felicidad', methods=['GET'])
def felicidad():
    mascota_id = request.args.get('mascota_id')
    # Obtener datos del microservicio de rastreo de felicidad
    response = requests.get(f'http://localhost:5003/felicidad/{mascota_id}')
    if response.status_code == 200:
        felicidad = response.json().get('felicidad')
        return jsonify({"felicidad": felicidad})
    else:
        return jsonify({"error": "Error al verificar la felicidad de la mascota"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # El frontend corre en el puerto 5000

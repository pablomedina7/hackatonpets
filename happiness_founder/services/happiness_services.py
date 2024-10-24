import requests
from datetime import datetime, timedelta

# URL del microservicio de alimentación
ALIMENTACION_SERVICE_URL = 'http://localhost:5002/alimentar'

def obtener_ultima_alimentacion(mascota_id):
    try:
        respuesta = requests.get(f"{ALIMENTACION_SERVICE_URL}/{mascota_id}")
        if respuesta.status_code == 200:
            data = respuesta.json()
            return data.get('fecha_alimentacion')
        else:
            return None
    except Exception as e:
        print(f"Error al obtener la última alimentación: {str(e)}")
        return None

def calcular_felicidad(mascota_id):
    # Obtener la última vez que se alimentó a la mascota
    ultima_alimentacion = obtener_ultima_alimentacion(mascota_id)

    if not ultima_alimentacion:
        return None

    # Convertir la fecha de alimentación a objeto datetime
    ultima_alimentacion_dt = datetime.strptime(ultima_alimentacion, '%Y-%m-%dT%H:%M:%S')

    # Calcular el tiempo que ha pasado desde la última alimentación
    tiempo_transcurrido = datetime.now() - ultima_alimentacion_dt

    # Lógica de felicidad
    if tiempo_transcurrido < timedelta(hours=6):
        return "Feliz"
    elif timedelta(hours=6) <= tiempo_transcurrido < timedelta(hours=12):
        return "Neutral"
    else:
        return "Triste"

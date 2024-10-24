import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("Alimentocion.db")
cursor = conexion.cursor()

# Consulta para verificar la existencia de alimentaciones
mascota_id = 2  # Cambia esto al ID que deseas verificar
cursor.execute('SELECT * FROM alimentacion WHERE mascota_id = ?', (mascota_id,))
registros = cursor.fetchall()

if registros:
    for registro in registros:
        print(f'ID: {registro[0]}, Mascota ID: {registro[1]}, Hora de Alimentación: {registro[2]}')
else:
    print(f'No hay registros de alimentación para la mascota ID: {mascota_id}')

# Cerrar conexión
conexion.close()

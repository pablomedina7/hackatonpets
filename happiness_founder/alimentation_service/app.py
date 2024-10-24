from flask import Flask
from routes.alimentation_routes import alimentacion_bp
from models.alimentationdb_model import db
from config import Config

app = Flask(__name__)

# Cargar configuración desde config.py
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)

# Registrar el blueprint de alimentacion
app.register_blueprint(alimentacion_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas de la base de datos si no existen
    app.run(port=5002)

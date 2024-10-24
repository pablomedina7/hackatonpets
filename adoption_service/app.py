from flask import Flask
from routes.adoption_routes import adopcion_bp
from models.adoptionbd_model import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Registrar rutas
app.register_blueprint(adopcion_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001)

from flask import Flask
from routes.alimentation_routes import alimentacion_bp
from models.alimentationdb_model import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(alimentacion_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5002)

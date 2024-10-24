from models.adoptionbd_model import db  # Asegúrate de que esta línea está correcta
from flask import Flask
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5001)

from flask import Flask
from routes.happiness_routes import happiness_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(happiness_bp)

if __name__ == '__main__':
    app.run(port=5003)

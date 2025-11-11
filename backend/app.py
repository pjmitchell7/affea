from flask import Flask
from flask_cors import CORS
from src.config import Config
from src.db import init_db, create_all
from src.routes.health import health_bp
from src.routes.auth import auth_bp
from src.routes.films import films_bp
from src.routes.dmca import dmca_bp


app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGIN"]}})


init_db(app)
create_all(app)


app.register_blueprint(health_bp, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(films_bp, url_prefix="/api/films")
app.register_blueprint(dmca_bp, url_prefix="/api")


if __name__ == "__main__":
app.run(host="0.0.0.0", port=8000, debug=True)

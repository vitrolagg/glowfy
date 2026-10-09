from flask import Flask

from app.config import DevConfig
from app.extensions import db, migrate

# Cria a aplicação da api
def create_app(config_class= DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Extensões
    db.init_app(app)
    from app import models        # Importa os modelos necessários para o migrate

    migrate.init_app(app, db)

    # Enpoint de check da api
    @app.get("/api/health")
    def health():
        return {"status": "ok"}, 200

    return app
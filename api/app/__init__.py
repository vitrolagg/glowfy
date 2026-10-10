from flask import Flask

from app.config import DevConfig
from app.extensions import db, migrate, jwt

from app.common.errors import register_error_handlers

# Cria a aplicação da api
def create_app(config_class= DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    """Extensões"""
    db.init_app(app)

    # Importa os modelos necessários para o migrate
    from app import models

    # Conecta o migrate ao app e ao banco
    migrate.init_app(app, db)

    # Conecta o JWT ao app
    jwt.init_app(app)

    # Registra os handlers de erros
    register_error_handlers(app)

    # Endpoint de check da api
    @app.get("/api/health")
    def health():
        return {"status": "ok"}, 200

    return app
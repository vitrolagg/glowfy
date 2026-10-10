"""
Arquivo __init__.py (pacote app)

Fábrica da aplicação: create_app monta o Flask, conecta as extensões e registra
handlers de erro, callbacks do JWT e blueprints.
"""

from flask import Flask

from app.config import DevConfig
from app.extensions import db, migrate, jwt

from app.common.errors import register_error_handlers

# Cria a aplicação da api
def create_app(config_class= DevConfig):
    """
    Cria e configura uma instância da aplicação.

    Args:
        config_class: classe de configuração a usar (DevConfig por padrão.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Extensões
    db.init_app(app)

    # Importa os modelos necessários para o migrate
    from app import models

    # Conecta o migrate ao app e ao banco
    migrate.init_app(app, db)

    # Conecta o JWT ao app
    jwt.init_app(app)

    # Importa a função que registra os callbacks do jwt
    from app.auth.jwt_callbacks import register_jwt_callbacks

    # registra os callbacks do jwt
    register_jwt_callbacks(jwt)

    # Registra os handlers de erros
    register_error_handlers(app)

    # Importa o blueprint de autenticação
    from app.auth.routes import auth_bp

    # Registra as rotas de autenticação com o prefixo
    app.register_blueprint(auth_bp, url_prefix= "/api/auth")

    # Endpoint de check da api
    @app.get("/api/health")
    def health():
        return {"status": "ok"}, 200

    return app
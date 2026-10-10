"""
Arquivo jwt_callbacks.py

Callbacks do flask-jwt-extended. A função register_jwt_callbacks é chamada no create_app e ensina
a biblioteca a carregar o usuário a partir do token e a responder os erros de token no padrão da API.


user_lookup_callback: converte o "sub" do token no usuário do banco, disponível nas rotas como current_user.

user_lookup_error_callback: token válido, mas o usuário não existe mais.

expired_token_callback: token expirado.

invalid_token_callback: token com assinatura ou formato inválido.

missing_token_callback: requisição sem o header Authorization.
"""

from flask import jsonify

from app.extensions import db
from app.models import User

# Ensina o flask a lidar com usuários e erros desta API
def register_jwt_callbacks(jwt):

    # Chamado em toda rota com @jwt_required: converte o token em usuário
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):

        # O "sub" do token é o id do usuário em string
        user_id = int(jwt_data["sub"])

        # Busca no banco; o resultado vira o current_user
        return db.session.get(User, user_id)

    # Token válido, mas o lookup devolveu None
    @jwt.user_lookup_error_loader
    def user_lookup_error_callback(_jwt_header, _jwt_data):

        # Responde no padrão da API
        return jsonify(error="Usuário não encontrado"), 401

    # Token expirado
    @jwt.expired_token_loader
    def expired_token_callback(_jwt_header, _jwt_data):

        # Responde no padrão da API
        return jsonify(error="Token expirado"), 401

    # Token com assinatura ou formato inválido
    @jwt.invalid_token_loader
    def invalid_token_callback(_reason):

        # Responde no padrão da API
        return jsonify(error="Token inválido"), 401

    # Requisição sem o header Authorization
    @jwt.unauthorized_loader
    def missing_token_callback(_reason):

        # Responde no padrão da API
        return jsonify(error= "Token de acesso ausente"), 401
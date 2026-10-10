"""
Arquivo routes.py
"""

from flask import Blueprint, jsonify, request

from app.auth import services
from app.common.errors import ApiError

# Agrupa as rotas de autenticação
auth_bp = Blueprint("auth", __name__)

# Rota de login
@auth_bp.post("/login")
def login():

    # Lê o json do corpo
    payload = request.get_json(silent=True) or {}

    # Normaliza o email
    # O validate na classe User funciona apenas para insert e não em buscas
    email = (payload.get("email") or "").strip().lower()

    # Lê a senha
    password = payload.get("password")

    # Se faltou o email | se a senha não vier string | se a senha vier vazia
    if not email or not isinstance(password, str) or password== "":

        # Erro de formato
        raise ApiError(400, "email e senha são obrigatórios")

    # Delega para o service e responde
    return jsonify(services.login(email, password)), 200
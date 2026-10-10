"""
Arquivo routes.py

Rotas HTTP da autenticação, registradas no create_app com o prefixo /api/auth. Cuidam apenas
da parte HTTP: leem e validam o formato do corpo e delegam as regras para o services.py.


login (POST /login): valida e-mail e senha recebidos e devolve o access token gerado pelo services.login.

me (GET /me): rota protegida por token e restrida a usuários ativos; devolve os dados do usuário dono do token (current_user).
"""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import current_user, jwt_required

from app.auth import services
from app.common.errors import ApiError
from app.common.decorators import active_required

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
        raise ApiError(400, "Email e senha são obrigatórios")

    # Delega para o service e responde
    return jsonify(services.login(email, password)), 200

# Retorna os dados do usuário dono do token
@auth_bp.get("/me")
@jwt_required()
@active_required
def me():

    # current_user foi carregado pelo user_lookup_loader
    return jsonify(id=current_user.id, email=current_user.email), 200


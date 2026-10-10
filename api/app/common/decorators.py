"""
Arquivo decorators.py

Decorators reutilizáveis nas rotas da API. Rodam antes da rota e podem interromper a requisição.
"""

from functools import wraps

from flask import jsonify
from flask_jwt_extended import current_user

# Recebe a função da rota e devolve a versão protegida
def active_required(fn):
    "active_required: bloqueia com 403 o usuário desativado, mesmo que o token dele ainda seja válido. Deve ficar abaixo do @jwt_required(), que é quem carrega o current_user."

    # Mantém o nome e a docstring da rota original
    @wraps(fn)
    def wrapper(*args, **kwargs):

        # Se o usuário estiver desativado
        if not current_user.active:

            # Interrompe
            return jsonify(error="Usuário não autorizado"), 403

        # Usuário ativo
        return fn(*args, **kwargs)

    # Retorna a versão protegida
    return wrapper
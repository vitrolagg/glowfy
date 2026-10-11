"""
Arquivo: test_auth_service.py

Testes das regras de autenticação, usando o banco de testes
"""

import pytest

from flask_jwt_extended import decode_token

from app.extensions import db
from app.models import User
from app.common.errors import ApiError
from app.auth import services

# O login deve lançar exceção se o email não estiver cadastrado
def test_login_with_unknown_email_raises_401(db_user):

    # Captura a exceção
    with pytest.raises(ApiError) as exc_info:

        # Faz login com email não cadastrado
        services.login(email="outro@email.com", password="senha12345")

    # Código de erro esperado
    assert exc_info.value.status == 401

    # Mensagem esperada
    assert exc_info.value.message == "Credenciais inválidas"

# Senha incorreta deve lançar exceção
def test_login_with_wrong_password_raises_401(db_user):

    # Captura a exceção
    with pytest.raises(ApiError) as exc_info:

        # Faz login com senha incorreta
        services.login(email="teste@glowfy.com", password="Senha12345")

    # Código de erro esperado
    assert exc_info.value.status == 401

    # Mensagem esperada
    assert exc_info.value.message == "Credenciais inválidas"

# Credenciais corretas, usuário inativo
def test_login_with_inactive_user_raises_403(db_user):

    # Desativa o usuário no banco
    db_user.active = False
    db.session.commit()

    # Captura a exceção
    with pytest.raises(ApiError) as exc_info:

        # Faz login com as credenciais corretas
        services.login(email="teste@glowfy.com", password="senha12345")

    # Status esperado
    assert exc_info.value.status == 403

    # Mensagem esperada
    assert exc_info.value.message == "Usuário não autorizado"

# Tudo certo, testa o retorno
def test_login_returns_token_for_valid_credentials(db_user):

    # Faz login com as credenciais corretas
    result = services.login(email="teste@glowfy.com", password="senha12345")

    # O retorno deve ter o token de acesso
    assert "access_token" in result

    # Decodifica o token e obtém os dados
    payload = decode_token(result["access_token"])

    # O sub do token deve pertencer ao usuário correto
    assert payload["sub"] == str(db_user.id)
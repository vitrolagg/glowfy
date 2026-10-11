"""
Arquivo: conftest.py

Fixtures compartilhadas por todos os testes. O pytest carrega este arquivo automaticamente.
"""

import pytest

from app import create_app
from app.config import TestConfig
from app.extensions import db
from app.models import User
from app.auth.services import issue_token

@pytest.fixture
def app():
    """App com a configuração de testes e tabelas recém-criadas no banco de testes."""

    # Cria o app apontando para o banco de testes
    app = create_app(TestConfig)

    # Ativa o contexto do app
    with app.app_context():

        # Cria todas as tabelas a partir do models. Antes do teste.
        db.create_all()

        # Entrega o app para o teste; a fixture pausa aqui enquanto o teste roda
        yield app

        # Depois do teste: descarta a sessão e apaga todas as tabelas
        db.session.remove()
        db.drop_all()

@pytest.fixture
def db_user(app):
    """Usuário ativo salvo no banco de testes"""

    # Cria o usuário
    user = User(email="teste@glowfy.com")

    # Define a senha
    user.set_password("senha12345")

    # Salva no banco
    db.session.add(user)
    db.session.commit()

    return user

@pytest.fixture
def client(app):
    """Cliente HTTP de testes para requisições ao app sem subir servidor"""

    # Cria e retorna o cliente de testes a partir do app de testes
    return app.test_client()

@pytest.fixture
def auth_header(db_user):
    """Header Authorization com um token válido do db_user"""

    token = issue_token(db_user)["access_token"]

    return {"Authorization": f"Bearer {token}"}
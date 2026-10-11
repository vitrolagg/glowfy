"""
Arquivo: test_user.py

Testes do model User que não precisam de banco: normalização de email e hash de senha.
"""

import pytest

from app.models import User

# Fixture: prepara um usuário com senha definida
@pytest.fixture
def user():

    # Cria o usuário em memória
    user = User(email="teste@glowfy.com")

    # Define a senha
    user.set_password("senha12345")

    # Entrega o usuário para o teste
    return user

# A senha correta deve ser aceita
def test_check_password_accepts_correct_password(user):

    # A mesma senha deve conferir
    assert user.check_password("senha12345") is True

# A senha gravada deve ser hash
def test_set_password_does_not_store_plain_text(user):

    # Verifica se o que foi salvo não é a senha pura
    assert user.password_hash != "senha12345"

# O e-mail deve ser salvo sem espaços e em minúsculas
def test_email_is_normalized():

    # Cria o usuário com espaços e maiúsculas de propósito (não usa a fixture)
    user = User(email="  Teste@Glowfy.com ")

    # O @validates deve ter normalizado
    assert user.email == "teste@glowfy.com"

# Senha errada deve ser recusada
def test_check_password_rejects_wrong_password(user):
    
    # O retorno do check_password deve ser False
    assert user.check_password("Senha12345") is False
    
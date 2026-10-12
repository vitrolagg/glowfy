"""
Arquivo: test_services.py

Testes das regras dos usuários
"""

import pytest

from app.users import services
from app.extensions import db
from app.models import User
from app.common.errors import ApiError

# A função create_user deve criar o usuário no banco corretamente
def test_create_user_saves_user_with_hashed_password(app):

    # Email usado no teste
    email="teste@email.com"

    # Senha usada no teste
    password="senha12345"

    # Cria o usuário
    services.create_user(
        email=email,
        password= password
    )

    # Consulta o email no banco
    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    # O usuário criado deve ter ID
    assert user.id is not None

    # O email do usuário criado deve ser o mesmo passado na função.
    assert user.email == email

    # A senha passada na função deve bater com a do banco (hash)
    assert user.check_password(password)

# Um email que já existe no banco não deve ser criado outra vez
def test_create_user_with_duplicated_email_raises_409(app):

    # Email usado no teste
    email="teste@email.com"

    # Senha usada no teste
    password="senha12345"

    # Cria o usuário
    services.create_user(
        email=email,
        password= password
    )

    # Captura a exceção
    with pytest.raises(ApiError) as exc_info:

        # Tenta criar novamente com o mesmo email
        services.create_user(
            email=email,
            password= password
        )

    # Status esperado
    assert exc_info.value.status == 409

    # Mensagem esperada
    assert exc_info.value.message == "Email já cadastrado"

def test_create_user_with_unnormalized_duplicated_email_raises_409(app):

    # Email usado no teste
    email="teste@email.com"

    # Mesmo email não normalizado
    not_normalized_email = "  TEste@email.com  "

    # Senha usada no teste
    password="senha12345"

    # Cria o usuário
    services.create_user(
        email=email,
        password= password
    )

    # Captura a exceção
    with pytest.raises(ApiError) as exc_info:

        # Tenta criar novamente com o mesmo email não normalizado
        services.create_user(
            email=not_normalized_email,
            password= password
        )

    # Status esperado
    assert exc_info.value.status == 409

    # Mensagem esperada
    assert exc_info.value.message == "Email já cadastrado"

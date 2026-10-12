"""
Arquivo services.py

Regras de negócio dos usuários. Não conhece HTTP (request/jsonify): recebe dados, devolve dados
e lança ApiError quando uma regra é violada.
"""

from app.extensions import db
from app.common.errors import ApiError
from app.models import User

# Cria um usuário
def create_user(email: str, password: str) -> User:
    """Normaliza o email recebido, confere se já está sendo utilizado e cria usuário no banco"""

    # Normaliza o email antes da busca
    normalized_email = email.strip().lower()

    # Busca usuário no banco pelo email
    user = db.session.execute(db.select(User).filter_by(email=normalized_email)).scalar_one_or_none()

    # Se o email já estiver cadastrado
    if user:

        # Lança exceção
        raise ApiError(409, "Email já cadastrado")

    # Cria usuário
    user = User(email= normalized_email)

    # Define a senha
    user.set_password(password)

    # Salva no banco
    db.session.add(user)
    db.session.commit()

    # Retorna usuário criado
    return user
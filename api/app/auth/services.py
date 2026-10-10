"""
Arquivo services.py

Regras de negócio da autenticação. Não conhece HTTP (request/jsonify): recebe dados, devolve dados
e lança ApiError quando uma regra é violada.
"""


from flask_jwt_extended import create_access_token

from app.common.errors import ApiError
from app.extensions import db
from app.models import User

# Gera o token de acesso de um usuário
def issue_token(user: User) -> dict:
    """Gera o access token de um usuário, com o id dele no campo "sub"."""

    # O identity vira o campo "sub" do token
    access_token = create_access_token(
        # Converte o id do usuário para string
        identity=str(user.id)
    )

    # Retorna no formato da resposta
    return {"access_token": access_token}

# Confere as credenciais e devolve o token:
def login(email: str, password: str) -> dict:
    """Confere as credenciais (usuário existe, senha confere, usuário ativo) e devolve o token."""

    # Busca o usuário pelo email
    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    # Se não existir ou a senha não confere
    if user is None or not user.check_password(password):

        # Mensagem única para não revelar se o email existe
        raise ApiError(401, "Credenciais inválidas")

    # Se o usuário foi desativado
    if not user.active:

        # Bloqueia o login
        raise ApiError(403, "Usuário não autorizado")

    # Tudo certo: gera o token
    return issue_token(user)
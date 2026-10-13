"""
Arquivo user.py

Model da tabela users: credenciais de acesso dos membros da equipe.

A tabela ainda é parcial em relação ao modelo físico (docs/model): faltam unit_id,
staff_id e last_login_at, que serão adicionados conforme a necessidade.
"""

from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db
from sqlalchemy.orm import validates

# Perfis de acesso
ROLES = (
    "owner",
    "coordinator",
    "receptionist",
    "professional",
    "assistant"
)

# Perfis no formato sql
ROLES_SQL = ", ".join(f"'{role}'" for role in ROLES)

class User(db.Model):
    """
    Usuário com acesso ao sistema.

    A senha nunca é guardada em texto puro: use set_password para gravar o hash e
    check_password para conferir. O e-mail é normalizado (sem espaços, em minúsculas)
    sempre que é atribuído.
    """

    # Usa o nome users para esta tabela. Isso quebra convenção de entidades no singular mas é necessário pois "user" é uma palavra reservada no postgres
    __tablename__ = "users"

    # Restrições da tabela
    __table_args__ = (
        db.CheckConstraint(f"role IN ({ROLES_SQL})", name="ck_users_role"),
    )

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(160), nullable= False, unique= True, index= True)
    password_hash = db.Column(db.String(255), nullable= False)
    active = db.Column(db.Boolean, nullable= False, server_default=db.true())
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())

    # Normaliza o email
    @validates("email")
    def _normalize_email(self, key, value):

        # Remove espaços e converte para minúsculas
        return value.strip().lower()

    # Seta a senha
    def set_password(self, raw_password: str) -> None:
        """Gera o hash da senha e grava em password_hash."""

        self.password_hash = generate_password_hash(raw_password)

    # Checa a senha
    def check_password(self, raw_password: str) -> bool:
        """Confere se a senha informada corresponde ao hash gravado."""
        
        return check_password_hash(self.password_hash, raw_password)
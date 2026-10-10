from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db
from sqlalchemy.orm import validates

class User(db.Model):

    # Usa o nome users para esta tabela. Isso quebra convenção de entidades no singular mas é necessário pois "user" é uma palavra reservada no postgres
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(160), nullable= False, unique= True, index= True)
    password_hash = db.Column(db.String(255), nullable= False)
    active = db.Column(db.Boolean, nullable= False, server_default=db.true())
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())

    # Normaliza o email
    @validates("email")
    def _normalize_email(self, key, value):

        # Remove espaços e converte para minúsculas
        return value.strip().lower()

    # Seta a senha
    def set_password(self, raw_password: str) -> None:
        self.password_hash = generate_password_hash(raw_password)

    # Checa a senha
    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password_hash, raw_password)
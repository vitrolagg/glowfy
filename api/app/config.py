import os
from pathlib import Path
from datetime import timedelta

from dotenv import load_dotenv
from sqlalchemy import URL


# Diretório raiz da aplicação
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# carrega as variáveis de ambiente da API
load_dotenv(ROOT_DIR/"api"/".env")

# Carrega as variáveis de ambiente do banco de dados
load_dotenv(ROOT_DIR/"postgres"/".env")

# Monta a URL de conexão com o banco de dados
DATABASE_URL = URL.create(

    # Dialeto do banco
    drivername="postgresql",

    # Usuário do banco
    username=os.environ.get("POSTGRES_USER"),

    # Senha do banco (o URL.create já trata caracteres especiais como @ e :)
    password=os.environ.get("POSTGRES_PASSWORD"),

    # Host do banco (localhost no desenvolvimento, nome do serviço no Docker em produção)
    host=os.environ.get("POSTGRES_HOST", "localhost"),

    # Porta do banco (convertida para inteiro, padrão 5432)
    port=int(os.environ.get("POSTGRES_PORT", 5432)),

    # Nome do banco
    database=os.environ.get("POSTGRES_DB"),
)

# Configurações base
class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    # Banco de dados
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Tempo de vida do token de acesso jwt
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)

# Configurações de desenvolvimento
class DevConfig(BaseConfig):
    DEBUG = True
    
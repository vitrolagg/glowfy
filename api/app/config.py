"""
Arquivo config.py

Configurações da aplicação. Carrega as variáveis dos arquivos .env da API e do Postgres,
monta a URL do banco e define as classes de configuração usadas no create_app.
"""

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
    """Configurações comuns a todos os ambientes (chaves, banco e JWT)."""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    # Banco de dados
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Tempo de vida do token de acesso jwt
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)

# Configurações de desenvolvimento
class DevConfig(BaseConfig):
    """Configurações de desenvolvimento: herda a base e ativa o modo debug."""
    DEBUG = True

class TestConfig(BaseConfig):
    """Configurações dos testes: banco separado e chaves fixas, independentes do .env"""

    # Ativa o modo de teste do Flask
    TESTING = True

    # Mesmo servidor mas no banco de testes
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.set(database=f"{DATABASE_URL.database}_test")

    # Chaves fixas para os testes não dependerem do .env
    SECRET_KEY = "test-secret"
    JWT_SECRET_KEY = "test-jwt-secret-com-tamanho-suficiente-32"
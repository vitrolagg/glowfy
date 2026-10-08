import os

from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Configurações base
class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY")

# Configurações de desenvolvimento
class DevConfig(BaseConfig):
    DEBUG = True
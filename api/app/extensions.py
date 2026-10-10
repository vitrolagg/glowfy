"""
Arquivo extensions.py

Instâncias das extensões do Flask, criadas sem app. Ficam num arquivo separado para
evitar import circular: qualquer módulo pode importar daqui, e o create_app liga
cada uma ao app com init_app.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# ORM do banco de dados
db = SQLAlchemy()

# Migrations do banco (Alembic)
migrate = Migrate()

# Autenticação JWT
jwt = JWTManager()
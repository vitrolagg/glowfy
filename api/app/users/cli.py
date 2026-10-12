"""
Arquivo: cli.py

Comando para criar novo usuário no banco de dados via terminal.
"""

import click
from flask.cli import with_appcontext

from app.users import services
from app.common.errors import ApiError

# Cria um comando um usuário pedindo email e senha no terminal
@click.command("create-user")
@with_appcontext
def create_user_command():
    """Cria usuário novo no banco de dados"""

    # Input de email
    email = click.prompt("Email")

    # Input de senha
    password = click.prompt("Senha", hide_input=True, confirmation_prompt="Confirme a senha")

    # Tenta criar o usuário
    try:

        # Chama create_user do services
        user = services.create_user(email=email, password=password)

    # Em caso de erro
    except ApiError as e:

        # Lança erro no terminal
        raise click.ClickException(e.message)

    # Mostra no terminal
    click.echo(
        f"Usuário criado com sucesso\n"
        f"ID: {user.id} \n"
        f"Email: {user.email}" 
    )
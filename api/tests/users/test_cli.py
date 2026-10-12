"""
Arquivo test_cli.py

Teste dos comandos de terminal
"""

from app.users.cli import create_user_command

# O comando create-user do flask deve criar o usuário
def test_create_user_command_creates_user(runner):

    # Email usado no teste
    email = "ana@glowfy.com"

    # Senha usada no teste
    password = "senha12345"

    # Executa o comando simulando entrada no terminal
    result = runner.invoke(create_user_command, input=f"{email}\n{password}\n{password}\n")

    # O comando deve terminar sem erro
    assert result.exit_code == 0

    # O email do usuário criado deve aparecer na saída
    assert email in result.output

# Email já cadastrado deve encerrar o comando com mensagem de erro, sem traceback
def test_create_user_command_with_duplicated_email_shows_error(runner):

    # Email usado no teste
    email = "ana@glowfy.com"

    # Senha usada no teste
    password = "senha12345"

    # Executa o comando simulando entrada no terminal
    runner.invoke(create_user_command, input=f"{email}\n{password}\n{password}\n")

    # Executa novamente o comando com o mesmo email e salva em result
    result = runner.invoke(create_user_command, input=f"{email}\n{password}\n{password}\n")

    # O comando deve mostrar erro
    assert result.exit_code == 1

    # A mensagem de erro deve aparecer na saída
    assert "Email já cadastrado" in result.output
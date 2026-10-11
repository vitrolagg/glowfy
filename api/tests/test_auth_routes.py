"""
Arquivo: test_auth_routes.py

Testes das rotas de autenticação via test client do Flask, conferindo status HTTP e corpo JSON.
"""

# Login com credenciais corretas deve responder 200 com o token
def test_login_route_returns_200_and_token(client, db_user):

    # Faz a requisição POST com o json de login
    response = client.post("/api/auth/login", json={
        "email": "teste@glowfy.com",
        "password":"senha12345"
    })

    # Status esperado
    assert response.status_code == 200

    # O corpo da resposta deve ter o token
    assert "access_token" in response.get_json()

# Login com senha incorreta deve responder 401
def test_login_with_wrong_password_returns_401(client, db_user):

    # Faz a requisição com a senha incorreta
    response = client.post("/api/auth/login", json={
        "email": "teste@glowfy.com",
        "password":"Senha12345"
    })

    # Status esperado
    assert response.status_code == 401

    # Corpo esperado
    assert response.get_json() == {"error": "Credenciais inválidas"}

# Login sem senha deve responder 400
def test_login_without_password_returns_400(client):

    # Faz login sem enviar a senha
    response = client.post("/api/auth/login", json={
        "email": "teste@glowfy.com",
    })

    # Stats esperado
    assert response.status_code == 400

    # Corpo esperado
    assert response.get_json() == {"error": "Email e senha são obrigatórios"}

# Login com email correto mas não normalizado deve responder 200
def test_login_with_unnormalized_email_returns_200(client, db_user):

    # Faz login com email correto não normalizado
    response = client.post("/api/auth/login", json={
        "email": "   TEste@glowfy.com  ",
        "password": "senha12345"
    })

    # Status esperado
    assert response.status_code == 200

    # O corpo da resposta deve ter o token
    assert "access_token" in response.get_json()
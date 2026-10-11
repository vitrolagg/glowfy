"""
Arquivo: test_routes.py

Testes das rotas de autenticação via test client do Flask, conferindo status HTTP e corpo JSON.
"""

from datetime import timedelta

from app.extensions import db
from flask_jwt_extended import create_access_token

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

    # Status esperado
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


# Token válido deve responder 200 com os dados do usuário
def test_route_me_returns_200_and_user_data(client, db_user, auth_header):

    # Faz a requisição com o header de autorização
    response = client.get("/api/auth/me", headers= auth_header)

    # Status esperado
    assert response.status_code == 200

    # O corpo deve conter os dados do dono do token
    assert response.get_json() == {
        "id": db_user.id, 
        "email": "teste@glowfy.com"
    }

# Token ausente deve responder 401
def test_route_me_without_token_returns_401(client):

    # Faz a requisição sem o token
    response = client.get("/api/auth/me")

    # Status esperado
    assert response.status_code == 401

    # Corpo esperado
    assert response.get_json() == {"error": "Token de acesso ausente"}

# Token inválido deve responder 401
def test_route_me_with_invalid_token_returns_401(client):

    # Faz a requisição com um token inválido
    response = client.get("/api/auth/me", headers= {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIn0.4F7Mbr4_Lx4YFn9-r2OUuWvp-XCVXumq4Pdl2GqwAUU"})

    # Status esperado
    assert response.status_code == 401

    # Corpo esperado
    assert response.get_json() == {"error": "Token inválido"}


# Usuário inativo deve responder 403
def test_route_me_with_inactive_user_returns_403(client, db_user, auth_header):

    # Desativa o usuário no banco
    db_user.active = False
    db.session.commit()

    # Faz a requisição
    response = client.get("/api/auth/me", headers= auth_header)

    # Status esperado
    assert response.status_code == 403

    # Corpo esperado
    assert response.get_json() == {"error": "Usuário não autorizado"}

# Usuário não encontrado deve responder 401
def test_route_me_with_unknown_user_returns_401(client):

    # Cria token com id que não existe no banco de testes
    token = create_access_token(identity="900")

    # Faz requisição usando o token criado
    response = client.get("/api/auth/me", headers= {"Authorization": f"Bearer {token}"})

    # Status esperado
    assert response.status_code == 401

    # Corpo esperado
    assert response.get_json() == {"error": "Usuário não encontrado"}

# Token expirado deve responder 401
def test_route_me_with_expired_token_returns_401(client):

    # Cria token que expira em 2 segundos
    token = create_access_token(identity="1", expires_delta=timedelta(seconds=-1))

    # Faz requisição usando o token criado
    response = client.get("/api/auth/me", headers= {"Authorization": f"Bearer {token}"})

    # Status esperado
    assert response.status_code == 401
    
    # Corpo esperado
    assert response.get_json() == {"error": "Token expirado"}
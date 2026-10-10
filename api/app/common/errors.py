"""
Arquivo errors.py

Tratamento centralizado de erros da API. A função register_error_handlers é chamada no create_app
e registra os handlers abaixo. A classe ApiError é o tipo de exceção específico da api para erros esperados.


handle_api_error: captura os erros esperados da api (raise ApiError(status, mensagem)) e retorna
em JSON com o status e a mensagem informados.

handle_http_error: captura os erros HTTP padrão do Flask (404, 405...) e retorna em JSON
ao invés da página HTML, mantendo o código do próprio erro.
"""


from flask import jsonify
from werkzeug.exceptions import HTTPException

# Exceção própria da API: carrega o status HTTP e a mensagem
class ApiError(Exception):

    def __init__(self, status: int, message: str):

        # Inicializa a Exception normalmente
        super().__init__(message)

        # Código HTTP que será devolvido
        self.status = status

        # Mensagem que vai para o front
        self.message = message

# Registra no app as funções que convertem exceções em json
def register_error_handlers(app):

    # Sempre que um ApiError não for tratado em nenhum lugar, o Flask chama essa função
    @app.errorhandler(ApiError)
    def handle_api_error(error):

        # Monta a resposta com a mensagem e o status do erro
        return jsonify(error=error.message), error.status

    # Erros padrão do Flask também viram JSON em vez de página HTML
    @app.errorhandler(HTTPException)
    def handle_http_error(error):

        # Usa a descrição e o código do próprio erro
        return jsonify(error=error.description), error.code
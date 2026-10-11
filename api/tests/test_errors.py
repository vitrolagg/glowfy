"""
Arquivo: test_errors.py

Este arquivo contém testes para a classe ApiError, que é uma exceção personalizada usada para lidar com erros de API. Os testes verificam se a exceção armazena corretamente o código de status e a mensagem de erro, bem como se a mensagem corresponde ao esperado.
"""

import pytest

from app.common.errors import ApiError

# Testa se a ApiError guarda código e mensagem
def test_api_error_keeps_status_and_message():
    """Este teste verifica se a exceção ApiError armazena corretamente o código de status e a mensagem de erro. Ele força a exceção e, em seguida, verifica se os atributos status e message correspondem aos valores esperados."""

    # Lança o erro dentro do bloco e espera por ele
    with pytest.raises(ApiError) as exc_info:
        raise ApiError(404, "Não encontrado")

    # Verifica o código de erro
    assert exc_info.value.status == 404

    # Verifica a mensagem de erro
    assert exc_info.value.message == "Não encontrado"


# O str() do erro deve ser a mensagem
def test_api_error_str_returns_message():
    """Este teste verifica se a mensagem da exceção ApiError corresponde à mensagem esperada. Ele força a exceção e utiliza o parâmetro match do pytest.raises para verificar se a mensagem da exceção corresponde à string fornecida."""

    # O match compara o texto com o str() da exceção
    with pytest.raises(ApiError) as exc_info:
        raise ApiError(404, "Não encontrado")

    assert str(exc_info.value) == "Não encontrado"
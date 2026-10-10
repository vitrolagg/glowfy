"""
Arquivo run.py

Ponto de entrada da API em desenvolvimento: cria o app e sobe o servidor do Flask.
"""

from app import create_app

# Cria a aplicação
app = create_app()

# Se o arquivo for executado diretamente
if __name__ == "__main__":

    # Sobe o servidor
    app.run(host="0.0.0.0", port=8080)

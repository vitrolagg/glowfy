from app import create_app

# Cria a aplicação
app = create_app()

# Se o arquivo for executado diretamente
if __name__ == "__main__":

    # Sobe o servidor no localhost
    app.run(host="0.0.0.0", port=5000)
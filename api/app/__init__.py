from flask import Flask

from app.config import DevConfig

def create_app(config_class= DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.get("/api/health")
    def health():
        return {"status": "ok"}, 200

    return app
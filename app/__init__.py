from flask import Flask
from app.config import Config
from app.extensions import migrate, db
from app.produto.routes import produto_api
from app.user.routes import user_api

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_api)
    app.register_blueprint(produto_api)

    return app

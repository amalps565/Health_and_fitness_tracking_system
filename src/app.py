from flask import Blueprint, Flask, Response, g, jsonify
from flask_migrate import Migrate
from sqlalchemy import text

from .config.settings import settings
from .models import db, init_models
from .schemas import init_schemas, ma

def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(settings.flask_sqlalchemy_config)

    # Validate settings before initializing app
    settings.validate()

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    init_models()
    init_schemas()

    @app.before_request
    def before_request():
        # g.request_id = generate_request_id()
        pass

    @app.after_request
    def after_request(response):
        response.headers["X-Request-ID"] = getattr(g, "request_id", "")
        return response

    root_blueprint = Blueprint("root", __name__, url_prefix="/event-management")

    @root_blueprint.route("/health")
    def health() -> Response:
        return jsonify({"status": "UP", "service": "event-management", "db": check_db_connection()})

    def check_db_connection() -> str:
        try:
            # Execute a simple query to check DB connection
            db.session.execute(text("SELECT 1"))
            return "UP"
        except Exception as e:  # noqa
            return "DOWN"

    app.register_blueprint(root_blueprint)
    
    return app


if __name__ == "__main__":
    create_app().run()

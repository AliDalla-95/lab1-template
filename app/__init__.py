from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(in_memory_db=None):
    app = Flask(__name__)
    if in_memory_db:
        app.config['SQLALCHEMY_DATABASE_URI'] = in_memory_db
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "postgresql://persona_id_user:iRATS5GUXyzVmAj23poCXSbHcvZuovFE@dpg-cs0il423esus739369m0-a.frankfurt-postgres.render.com/persona_id"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from .routes import person_bp
    app.register_blueprint(person_bp)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/person-service.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Person Service API"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app

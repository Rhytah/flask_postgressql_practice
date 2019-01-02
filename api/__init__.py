from flask import Flask

from config import app_configuration


def create_app(mode):
    app = Flask(__name__)
    app.config.from_object(app_configuration)

    from api.views.user_views import auth
    from api.views.incident_views import incident

    app.register_blueprint(auth)
    app.register_blueprint(incident)

    return app

app = create_app(mode='development')

from flask import Flask

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    # Application Configuration
    # app.config.from_object("config.Config")

    with app.app_context():

        from . import routes

        return app


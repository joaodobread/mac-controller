import os
from flask import Flask
from src.api.controllers import home_page, volume_controller


def init_app(debug=False, use_reloader=False):
    print(f"Start using {debug=}, {use_reloader=}")
    app = Flask(__name__)
    app.use_reloader = use_reloader
    app.debug = debug
    app.register_blueprint(home_page)
    app.register_blueprint(volume_controller)
    return app


def run_app(app: Flask, host='0.0.0.0', port=5888):
    app.run(host=host, port=port)

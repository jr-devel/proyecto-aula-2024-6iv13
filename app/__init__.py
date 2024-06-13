import os
from flask import *
from werkzeug.utils import *
from .logger_base import log

def create_app():
    app = Flask(__name__)
    #
    from . import views
    app.register_blueprint(views.bp)
    #
    return app
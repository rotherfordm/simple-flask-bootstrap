import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
from config import Config
from flask import Flask

import waitress


app = Flask(__name__)
app.config.from_object(Config)

if not app.debug:
    if app.config["LOG_TO_STDOUT"]:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/application.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("Application startup")

from app import routes

port = int(os.environ.get('PORT', 80))
waitress.serve(app, port=port)
# 引用 flask 內建函式
from flask import Flask, g, render_template, request, redirect, url_for

# 引用其他相關模組
import os

from app.config.config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    register_extensions(app)
    register_blueprints(app)

    @app.route("/")
    def index():
        return "Hello Flask"

    return app


def register_extensions(app):
    """Register extensions with the Flask application."""
    # db.init_app(app)
    pass


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    # from .views.rss import category
    # app.register_blueprint(category, url_prefix="/category")
    pass

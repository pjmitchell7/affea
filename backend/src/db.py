from flask_sqlalchemy import SQLAlchemy
from flask import current_app


db = SQLAlchemy()


def init_db(app):
db.init_app(app)


def create_all(app):
with app.app_context():
from .models import User, Film, Watchlist
db.create_all()


# simple CLI helper
def db_up():
from .models import User, Film, Watchlist
db.create_all()

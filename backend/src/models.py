from datetime import datetime
from .db import db


class User(db.Model):
__tablename__ = "users"
id = db.Column(db.Integer, primary_key=True)
email = db.Column(db.String(255), unique=True, nullable=False)
password_hash = db.Column(db.String(255), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Film(db.Model):
__tablename__ = "films"
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(255), nullable=False)
description = db.Column(db.Text, nullable=True)
genre = db.Column(db.String(64), nullable=True)
runtime_min = db.Column(db.Integer, nullable=True)
thumbnail_url = db.Column(db.String(1024), nullable=True)
s3_key = db.Column(db.String(1024), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Watchlist(db.Model):
__tablename__ = "watchlists"
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
film_id = db.Column(db.Integer, db.ForeignKey("films.id"), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)

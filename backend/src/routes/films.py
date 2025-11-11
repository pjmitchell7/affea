from flask import Blueprint, request, jsonify
from ..db import db
from ..models import Film
from ..services.s3 import presign_key


films_bp = Blueprint("films", __name__)


@films_bp.get("")
def list_films():
films = Film.query.order_by(Film.created_at.desc()).all()
out = [
{
"id": f.id,
"title": f.title,
"description": f.description,
"thumbnail_url": f.thumbnail_url,
"runtime_min": f.runtime_min,
}
for f in films
]
return jsonify(out)


@films_bp.post("")
def create_film():
data = request.get_json()
film = Film(
title=data.get("title"),
description=data.get("description"),
genre=data.get("genre"),
runtime_min=data.get("runtime_min"),
thumbnail_url=data.get("thumbnail_url"),
s3_key=data.get("s3_key"),
)
db.session.add(film)
db.session.commit()
return jsonify({"id": film.id}), 201


@films_bp.get("/<int:film_id>/stream")
def stream_url(film_id: int):
film = Film.query.get_or_404(film_id)
url = presign_key(film.s3_key)
return jsonify({"url": url})

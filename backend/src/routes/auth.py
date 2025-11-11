from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from ..db import db
from ..models import User
from flask import current_app as app


jwt = JWTManager()


auth_bp = Blueprint("auth", __name__)


@auth_bp.record
def setup_jwt(setup_state):
jwt.init_app(setup_state.app)


@auth_bp.post("/register")
def register():
data = request.get_json()
email = data.get("email")
password = data.get("password")
if not email or not password:
return jsonify({"error": "Email and password required"}), 400
if User.query.filter_by(email=email).first():
return jsonify({"error": "Email already registered"}), 409
user = User(email=email, password_hash=generate_password_hash(password))
db.session.add(user)
db.session.commit()
return jsonify({"message": "ok"}), 201


@auth_bp.post("/login")
def login():
data = request.get_json()
email = data.get("email")
password = data.get("password")
user = User.query.filter_by(email=email).first()
if not user or not check_password_hash(user.password_hash, password):
return jsonify({"error": "Invalid credentials"}), 401
token = create_access_token(identity=str(user.id))
return jsonify({"access_token": token})

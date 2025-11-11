from flask import Blueprint, request, jsonify


dmca_bp = Blueprint("dmca", __name__)


@dmca_bp.post("/takedown")
def takedown():
# Store notice payload for review. Extend later with email workflow.
payload = request.get_json() or {}
return jsonify({"received": True, "payload": payload}), 202

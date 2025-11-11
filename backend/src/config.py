import os
class Config:
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ.get("JWT_SECRET", "change_me")
CORS_ORIGIN = os.environ.get("CORS_ORIGIN", "http://localhost:3000")
AWS_REGION = os.environ.get("AWS_REGION")
AWS_S3_BUCKET = os.environ.get("AWS_S3_BUCKET")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

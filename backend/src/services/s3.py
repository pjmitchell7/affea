import boto3
import os


region = os.environ.get("AWS_REGION")
bucket = os.environ.get("AWS_S3_BUCKET")
access_key = os.environ.get("AWS_ACCESS_KEY_ID")
secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


_s3 = boto3.client(
"s3",
region_name=region,
aws_access_key_id=access_key,
aws_secret_access_key=secret_key,
)


def presign_key(key: str, expires_in: int = 3600) -> str:
return _s3.generate_presigned_url(
ClientMethod="get_object",
Params={"Bucket": bucket, "Key": key},
ExpiresIn=expires_in,
)

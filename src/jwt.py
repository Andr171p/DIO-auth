from datetime import datetime, timedelta, timezone

from jose import jwt

from src.settings import AuthSettings


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"expire": expire})
    auth_data = ...
    encode_jwt = jwt.encode(to_encode, auth_data["secret_key"], algorithm=auth_data["algorithm"])
    return encode_jwt

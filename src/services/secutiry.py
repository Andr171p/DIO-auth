from jose import jwt
from datetime import datetime, timedelta, timezone

from src.settings import AuthSettings


class AccessTokenCreator:
    def __init__(self, auth_settings: AuthSettings) -> None:
        self._secret_key = auth_settings.secret_key
        self._algorithm = auth_settings.algorithm

    def __call__(self, data: dict, expires_delta: timedelta) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"expire": expire})
        return jwt.encode(to_encode, self._secret_key, algorithm=self._algorithm)

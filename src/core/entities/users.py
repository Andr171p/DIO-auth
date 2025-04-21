import uuid

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    public_id: uuid.UUID
    email: EmailStr
    hashed_password: str

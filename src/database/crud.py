import uuid
from typing import Any, Sequence, Optional

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserModel


class UserCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, user: UserModel) -> int:
        self._session.add(user)
        await self._session.flush()
        id = user.id
        await self._session.commit()
        return id

    async def read(self, id: int) -> Optional[UserModel]:
        stmt = (
            select(UserModel)
            .where(UserModel.id == id)
        )
        user = await self._session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_by_public_id(self, public_id: uuid.UUID) -> Optional[UserModel]:
        stmt = (
            select(UserModel)
            .where(UserModel.public_id == public_id)
        )
        user = await self._session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_by_email(self, email: str) -> Optional[UserModel]:
        stmt = (
            select(UserModel)
            .where(UserModel.email == email)
        )
        user = await self._session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_all(self) -> Sequence[UserModel]:
        stmt = select(UserModel)
        users = await self._session.execute(stmt)
        return users.scalars().all()

    async def update(self, id: int, **kwargs: Any) -> Optional[UserModel]:
        stmt = (
            update(UserModel)
            .where(UserModel.id == id)
            .values(**kwargs)
            .returning(UserModel)
        )
        user = await self._session.execute(stmt)
        await self._session.commit()
        return user.scalar_one_or_none()

    async def delete(self, id: int) -> Optional[UserModel]:
        stmt = (
            delete(UserModel)
            .where(UserModel.id == id)
        )
        user = await self._session.execute(stmt)
        await self._session.commit()
        return user.scalar_one_or_none()

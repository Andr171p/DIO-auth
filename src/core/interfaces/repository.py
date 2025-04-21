from typing import Optional
from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseRepository(ABC):
    @abstractmethod
    async def save(self, model: BaseModel) -> int:
        raise NotImplemented

    @abstractmethod
    async def get(self, id: int) -> Optional[BaseModel]:
        raise NotImplemented

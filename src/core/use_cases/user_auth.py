from src.core.interfaces import BaseRepository


class UserAuth:
    def __init__(self, repository: BaseRepository) -> None:
        self._repository = repository

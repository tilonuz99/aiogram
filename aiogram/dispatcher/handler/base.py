from abc import ABC, abstractmethod
from typing import Any, Dict

from aiogram import Bot
from aiogram.api.types import TelegramObject


class BaseHandlerMixin:
    event: TelegramObject
    data: Dict[str, Any]


class _HandlerBotMixin(BaseHandlerMixin):
    @property
    def bot(self) -> Bot:
        if "bot" in self.data:
            return self.data["bot"]
        return Bot.get_current()


class BaseHandler(_HandlerBotMixin, ABC):
    event: TelegramObject

    def __init__(self, event: TelegramObject, **kwargs: Any) -> None:
        self.event = event
        self.data = kwargs

    @abstractmethod
    async def handle(self) -> Any:  # pragma: no cover
        pass

    def __await__(self):
        return self.handle().__await__()

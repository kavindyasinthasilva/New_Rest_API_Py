from abc import ABC, abstractmethod
from typing import List, Any
from contextlib import AbstractContextManager

from services.ping.ping_services import PingService


class MyServiceInterface(PingService):
    @abstractmethod
    def do(self, ctx: AbstractContextManager, arg: List[Any]) -> List[Any]:
        pass

import logging
import os
from typing import List, Any, Tuple
from contextlib import AbstractContextManager

from flask import Flask

from config.logs import configure_logging

app = Flask(__name__)
logger = configure_logging()


class PingService:
    def do(self, ctx: AbstractContextManager, arg: List[Any]) -> tuple[list[str], str]:
        err = ''
        pinging = ["pinging"]
        logger.info(
            "pinging"
        )
        return pinging, err

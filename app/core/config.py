import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class Config:
    def __init__(self):
        self.init_logger()

    def init_logger(self):
        os.makedirs("logs", exist_ok=True)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        log_filename = f"logs/logs_{datetime.now().strftime('%Y-%m-%d')}.log"

        handler = TimedRotatingFileHandler(
            log_filename,
            when="midnight",
            interval=1,
            backupCount=7,
            encoding="utf-8",
            utc=False
        )
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        handler.suffix = "%Y-%m-%d"

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


config = Config()
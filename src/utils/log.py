import logging
import os

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        level=getattr(logging, log_level, logging.INFO),
    )


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    return logger
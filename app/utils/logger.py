import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("healthdax")
logger.setLevel(logging.INFO)

# -------- INFO LOG FILE --------
info_handler = RotatingFileHandler(
    f"{LOG_DIR}/app.log",
    maxBytes=5*1024*1024,
    backupCount=3
)
info_handler.setLevel(logging.INFO)

# -------- ERROR LOG FILE --------
error_handler = RotatingFileHandler(
    f"{LOG_DIR}/error.log",
    maxBytes=5*1024*1024,
    backupCount=3
)
error_handler.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)
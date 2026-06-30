import logging
import os
import config

os.makedirs(config.LOG_FOLDER, exist_ok=True)

log_path = os.path.join(config.LOG_FOLDER, config.LOG_FILE)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def get_logger():
    return logging.getLogger(config.APP_NAME)
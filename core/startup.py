import config
from services.logger import get_logger

logger = get_logger()


def start():
    print("=" * 50)
    print(f"{config.APP_NAME} AI Assistant")
    print(f"Version : {config.VERSION}")
    print("=" * 50)

    print(f"Welcome, {config.OWNER}.")

    logger.info("DON Started")

    print("System Ready.")
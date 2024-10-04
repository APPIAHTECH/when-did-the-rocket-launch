import os

from dotenv import load_dotenv

from utils.constants import Environment

load_dotenv()


class Config:
    ENVIRONMENT: Environment = Environment.use_env(os.getenv("ENVIRONMENT"))
    TITLE: str = "When did the Rocket Launch"
    APP_VERSION: str = "1.0.0"


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_BOT_USERNAME = os.getenv("TELEGRAM_BOT_USERNAME")

settings = Config()

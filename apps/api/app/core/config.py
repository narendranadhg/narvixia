from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Narvixia API")
    APP_ENV = os.getenv("APP_ENV", "development")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    DATABASE_URL = os.getenv("DATABASE_URL", "")

    SECRET_KEY = os.getenv("SECRET_KEY", "")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")


settings = Settings()
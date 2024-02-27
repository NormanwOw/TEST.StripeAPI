import stripe
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env-non-dev')

    DEBUG: int

    SECRET_KEY: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    STRIPE_PUBLISHABLE_KEY: str
    STRIPE_SECRET_KEY: str


settings = Settings()

DOMAIN_URL = 'http://localhost:8000/'

stripe.api_key = settings.STRIPE_SECRET_KEY

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_ENDPOINT_PROVIDER_1: str
    X_API_KEY_PROVIDER_1: str
    API_ENDPOINT_PROVIDER_2: str
    X_API_KEY_PROVIDER_2: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

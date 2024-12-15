from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = 'qwerty'
    ALGORITHM: str = 'HS256'
    API_KEY: str = 'luKBWbLiYbZWT2nU8wR5Cy2eExG76w4D'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()

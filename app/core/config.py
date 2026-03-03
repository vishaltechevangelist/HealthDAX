from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_ENV: str
    APP_NAME: str 
    # API_V1_PREFIX : str 

    LLM_MODEL_NAME: str 
    LLM_SRV_URL: str 
    DATASET_FILE_PATH: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
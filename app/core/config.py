from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = 'HealthDAX API'
    API_V1_PREFIX : str = '/api/v1'

    LLM_MODEL_NAME: str = 'ollama/llama3'
    LLM_SRV_URL: str = 'http://127.0.0.1:11434'
    DATASET_FILE_PATH: str = 'data'

@lru_cache()
def get_settings():
    return Settings()
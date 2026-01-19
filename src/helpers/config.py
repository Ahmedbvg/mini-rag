# src/helpers/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from enum import Enum
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), '../.env'),
        env_file_encoding='utf-8',
        extra='ignore'
    )
    
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list = Field(default=["text/plain", "application/pdf"])
    FILE_MAX_SIZE: int = Field(default=10)
    FILE_DEFAULT_CHUNK_SIZE: int = Field(default=512000)
    MONGODB_URL: str
    MONGODB_DATABASE: str

def get_settings():  
    return Settings()
# ⬇ Add this at the end of the file
class DataBaseEnum(Enum):
    COLLECTION_PROJECTS_NAME = "projects"
    COLLECTION_CHUNK_NAME = "chunks"
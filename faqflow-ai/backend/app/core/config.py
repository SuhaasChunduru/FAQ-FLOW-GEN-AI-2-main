import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "FAQFlow AI"
    API_V1_STR: str = "/api/v1"
    
    # SECURITY
    SECRET_KEY: str = "super-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # DATABASE
    DATABASE_URL: str = "sqlite:///./faqflow.db"
    
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        # Render hands out postgresql://, which SQLAlchemy maps to psycopg2.
        # Only psycopg3 is installed, so point it at that driver instead.
        return self.DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)
    
    # CHROMA DB
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: str = "8000"
    
    # GEMINI
    GEMINI_API_KEY: str = ""

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env", extra="ignore")

settings = Settings()

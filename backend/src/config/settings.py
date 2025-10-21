"""
Backend service configuration settings
"""
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Backend service configuration"""

    # Server Settings
    host: str = Field(default="127.0.0.1", description="Server host address")
    port: int = Field(default=8000, ge=1024, le=65535, description="Server port")
    reload: bool = Field(default=True, description="Enable hot reload")
    log_level: str = Field(default="info", description="Logging level")

    # CORS Settings
    cors_origins: List[str] = Field(
        default=["http://localhost:3000"],
        description="CORS allowed origins"
    )

    # Security
    secret_key: str = Field(default="your-secret-key-here", description="Application secret key")
    debug: bool = Field(default=True, description="Debug mode")

    # Environment
    environment: str = Field(default="development", description="Current environment")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()
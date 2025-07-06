"""
Configuration module for AI Content Studio

This module handles all configuration settings including:
- Environment variables
- Database connections
- API keys and secrets
- Application settings
"""

import os
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseModel):
    """Application settings with validation and defaults"""
    
    # OpenAI Configuration
    openai_api_key: str
    openai_model: str = "gpt-4"
    
    # Database Configuration
    database_url: str
    
    # Redis Configuration
    redis_url: str = "redis://localhost:6379"
    
    # Security Configuration
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Application Configuration
    debug: bool = True
    log_level: str = "INFO"
    max_workers: int = 4
    
    # Content Studio Configuration
    default_content_type: str = "article"
    max_content_length: int = 5000
    content_review_enabled: bool = True
    
    @classmethod
    def from_env(cls) -> "Settings":
        """Create settings from environment variables"""
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
            database_url=os.getenv("DATABASE_URL", ""),
            secret_key=os.getenv("SECRET_KEY", ""),
            openai_model=os.getenv("OPENAI_MODEL", "gpt-4"),
            redis_url=os.getenv("REDIS_URL", "redis://localhost:6379"),
            algorithm=os.getenv("ALGORITHM", "HS256"),
            access_token_expire_minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")),
            debug=os.getenv("DEBUG", "True").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            max_workers=int(os.getenv("MAX_WORKERS", "4")),
            default_content_type=os.getenv("DEFAULT_CONTENT_TYPE", "article"),
            max_content_length=int(os.getenv("MAX_CONTENT_LENGTH", "5000")),
            content_review_enabled=os.getenv("CONTENT_REVIEW_ENABLED", "True").lower() == "true"
        )


# Global settings instance
settings = Settings.from_env()


def get_settings() -> Settings:
    """Get application settings instance"""
    return settings


def validate_environment() -> bool:
    """
    Validate that all required environment variables are set
    
    Returns:
        bool: True if all required variables are set, False otherwise
    """
    required_vars = [
        "OPENAI_API_KEY",
        "DATABASE_URL",
        "SECRET_KEY"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"Missing required environment variables: {', '.join(missing_vars)}")
        return False
    
    return True 
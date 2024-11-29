# app/config.py

from pydantic_settings import BaseSettings
from typing import Dict, Any, List, Optional
from functools import lru_cache
import json
import os
from datetime import datetime

class Settings(BaseSettings):
    # API Configuration
    BASE_URL: str = "http://llm_service:5000/"
    API_VERSION: str = "v1.0"
    PROJECT_NAME: str = "LLM Gateway"
    DEBUG: bool = False
    
    # Service Configuration
    LOG_LEVEL: str = "INFO"
    ENVIRONMENT: str = "development"
    ENABLE_SWAGGER: bool = True
    CORS_ORIGINS: List[str] = ["*"]
    
    # Model Configuration
    DEFAULT_MODEL: str = "gpt-3.5-turbo"
    CONTEXT_LENGTH: int = 2000
    TEMPERATURE: float = 0.7
    
    # Security Settings
    API_KEY: str = "your_api_key_here"
    
    # Endpoint Configuration
    ENDPOINTS: Dict[str, Dict[str, Any]] = {
        "generate_llama": {
            "path": "/generate-llama-response",
            "method": "POST",
            "timeout": 30
        },
        "generate_standard": {
            "path": "/generate-response",
            "method": "POST",
            "timeout": 30
        }
    }

    # Feature Flags Configuration
    FEATURE_FLAGS_FILE: str = "feature_flags.json"
    ENABLE_LLAMA: bool = True
    ENABLE_STANDARD: bool = True
    ENABLE_LOGGING: bool = True

    class Config:
        env_file = ".env"
        extra = "allow"  # Permite campos adicionales en el .env

    def get_endpoint_url(self, endpoint_name: str) -> str:
        """Construye la URL completa para un endpoint específico."""
        endpoint_config = self.ENDPOINTS.get(endpoint_name)
        if not endpoint_config:
            raise ValueError(f"Endpoint {endpoint_name} not found in configuration")
        return f"{self.BASE_URL}/{self.API_VERSION}/llm{endpoint_config['path']}"

    def get_timeout(self, endpoint_name: str) -> int:
        """Obtiene el timeout para un endpoint específico."""
        endpoint_config = self.ENDPOINTS.get(endpoint_name)
        if endpoint_config:
            return endpoint_config.get("timeout", 30)
        return 30

@lru_cache()
def get_settings() -> Settings:
    """Retorna una instancia cacheada de la configuración."""
    return Settings()

# Instancia global de configuración
settings = get_settings()

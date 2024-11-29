from fastapi import APIRouter, HTTPException, status
from app.config import settings
from app.services.generation_service import GenerationService
import httpx
from typing import Dict, Any
import logging
from pydantic import BaseModel, Field
from datetime import datetime

# Configurar logger
logger = logging.getLogger(__name__)
router = APIRouter()

# Modelos Pydantic
class LlamaRequest(BaseModel):
    maxLength: int = Field(default=0)
    temperature: float = Field(default=0)
    text: str

    class Config:
        schema_extra = {
            "example": {
                "maxLength": 0,
                "temperature": 0,
                "text": "What is the capital of France?"
            }
        }

class StandardRequest(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "What is the capital of France?"
            }
        }

class LLMResponse(BaseModel):
    response: Dict[str, Any]

@router.post(
    "/generate-llama-response",
    response_model=LLMResponse,
    summary="Genera una respuesta usando el modelo Llama"
)
async def generate_llama_response(request: LlamaRequest):
    """Endpoint para generar respuestas usando el modelo Llama."""
    generation_service = GenerationService()
    return await generation_service.generate_llama_response(request)

@router.post(
    "/generate-response",
    response_model=LLMResponse,
    summary="Genera una respuesta usando el modelo predeterminado"
)
async def generate_response(request: StandardRequest):
    """Endpoint para generar respuestas usando el modelo predeterminado."""
    generation_service = GenerationService()
    return await generation_service.generate_standard_response(request)

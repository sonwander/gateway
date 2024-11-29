from typing import Dict, Any
import httpx
from fastapi import HTTPException, status
import logging
from app.config import settings

logger = logging.getLogger(__name__)

class GenerationService:
    """Servicio para manejar la generación de respuestas LLM."""

    async def _make_llm_request(self, url: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza una llamada HTTP al endpoint LLM."""
        async with httpx.AsyncClient() as client:
            try:
                logger.info(f"Making request to {url}")
                headers = {
                    "Content-Type": "application/json",
                }

                response = await client.post(
                    url,
                    json=payload,
                    headers=headers,
                    timeout=settings.get_timeout("generate_llama")
                )
                response.raise_for_status()

                return response.json()
            except httpx.HTTPError as e:
                logger.error(f"HTTP error occurred: {str(e)}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Error calling LLM service: {str(e)}"
                )
            except Exception as e:
                logger.error(f"Error occurred: {str(e)}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=str(e)
                )

    async def generate_llama_response(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Genera una respuesta usando el modelo Llama."""
        try:
            url = settings.get_endpoint_url("generate_llama")
            payload = {
                "maxLength": request.maxLength,
                "temperature": request.temperature,
                "text": request.text
            }

            response = await self._make_llm_request(url, payload)
            return {"response": response}

        except Exception as e:
            logger.error(f"Error in generate_llama_response: {str(e)}")
            raise

    async def generate_standard_response(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Genera una respuesta usando el modelo predeterminado."""
        try:
            url = settings.get_endpoint_url("generate_standard")
            payload = {
                "text": request.text
            }

            response = await self._make_llm_request(url, payload)
            return {"response": response}

        except Exception as e:
            logger.error(f"Error in generate_standard_response: {str(e)}")
            raise

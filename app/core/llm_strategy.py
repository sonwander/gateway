from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from pydantic import BaseModel

class LLMResponse(BaseModel):
    text: str
    tokens_used: Optional[int] = None
    metadata: Dict[str, Any] = {}

class LLMStrategy(ABC):
    """Clase base abstracta para estrategias de LLM."""

    @abstractmethod
    async def generate(
        self,
        text: str,
        **kwargs
    ) -> LLMResponse:
        """
        Genera una respuesta basada en el texto de entrada.
        
        Args:
            text: Texto de entrada
            **kwargs: Argumentos adicionales específicos del modelo
            
        Returns:
            LLMResponse: Respuesta generada
        """
        pass

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """
        Obtiene información sobre el modelo.
        
        Returns:
            Dict[str, Any]: Información del modelo
        """
        pass

class LlamaStrategy(LLMStrategy):
    """Implementación de la estrategia para el modelo Llama."""

    async def generate(
        self,
        text: str,
        max_length: int = 100,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        # Aquí iría la implementación real de la llamada al modelo Llama
        try:
            # Simulación de respuesta
            response = "This is a simulated Llama response"
            return LLMResponse(
                text=response,
                tokens_used=len(response.split()),
                metadata={
                    "max_length": max_length,
                    "temperature": temperature
                }
            )
        except Exception as e:
            raise Exception(f"Error generating Llama response: {str(e)}")

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "name": "llama",
            "version": "2.0",
            "capabilities": ["text-generation", "chat"],
            "max_length": 2048,
            "supported_languages": ["en", "es"]
        }

class GPTStrategy(LLMStrategy):
    """Implementación de la estrategia para modelos GPT."""

    async def generate(
        self,
        text: str,
        **kwargs
    ) -> LLMResponse:
        # Aquí iría la implementación real de la llamada al modelo GPT
        try:
            # Simulación de respuesta
            response = "This is a simulated GPT response"
            return LLMResponse(
                text=response,
                tokens_used=len(response.split()),
                metadata=kwargs
            )
        except Exception as e:
            raise Exception(f"Error generating GPT response: {str(e)}")

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "name": "gpt-3.5-turbo",
            "version": "1.0",
            "capabilities": ["text-generation", "chat", "completion"],
            "max_length": 4096,
            "supported_languages": ["en", "es", "fr", "de"]
        }

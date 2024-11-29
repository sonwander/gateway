from typing import Dict, Optional, Type
from app.core.llm_strategy import LLMStrategy
import logging

logger = logging.getLogger(__name__)

class LLMRegistry:
    _instance = None
    _models: Dict[str, LLMStrategy] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMRegistry, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Inicializa el registro de modelos LLM."""
        # Aquí se registrarían los diferentes modelos
        pass

    @classmethod
    def register_model(cls, name: str, strategy: Type[LLMStrategy]) -> None:
        """Registra un nuevo modelo LLM."""
        if name not in cls._models:
            cls._models[name] = strategy()
            logger.info(f"Model {name} registered successfully")

    def get_model(self, name: str) -> Optional[LLMStrategy]:
        """Obtiene una instancia de un modelo LLM."""
        return self._models.get(name)

    @classmethod
    def reload_registry(cls) -> None:
        """Recarga el registro de modelos."""
        cls._models.clear()
        if cls._instance:
            cls._instance._initialize()

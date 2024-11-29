from typing import Dict, Any
import json
import logging
from app.config import settings

logger = logging.getLogger(__name__)

class FeatureFlags:
    """Gestiona los feature flags del sistema."""

    _instance = None
    _flags: Dict[str, bool] = {
        "enable_llama": True,
        "enable_standard": True,
        "enable_logging": True,
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FeatureFlags, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Inicializa los feature flags desde el archivo de configuración."""
        self._load_flags()

    def _load_flags(self):
        """Carga los flags desde el archivo JSON."""
        try:
            if settings.FEATURE_FLAGS_FILE:
                with open(settings.FEATURE_FLAGS_FILE, 'r') as f:
                    stored_flags = json.load(f)
                    self._flags.update(stored_flags)
                    logger.info("Feature flags loaded successfully")
        except Exception as e:
            logger.error(f"Error loading feature flags: {e}")

    def is_enabled(self, flag_name: str) -> bool:
        """Verifica si un feature flag está habilitado."""
        return self._flags.get(flag_name, False)

    def get_all_flags(self) -> Dict[str, bool]:
        """Obtiene todos los feature flags y sus estados."""
        return self._flags.copy()

# Instancia global de feature flags
feature_flags = FeatureFlags()

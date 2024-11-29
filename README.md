# LLM Gateway

Este proyecto implementa un gateway para servicios LLM (Large Language Models) utilizando FastAPI.

## Estructura del Proyecto

```
llm_gateway/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── llm.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── llm_strategy.py
│   │   ├── feature_flags.py
│   │   ├── llm_registry.py
│   │   └── models.py
│   └── services/
│       ├── __init__.py
│       ├── sentiment_service.py
│       ├── contextualization_service.py
│       ├── customization_service.py
│       ├── evaluation_service.py
│       ├── generation_service.py
│       └── training_service.py
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_sentiment.py
│   ├── test_contextualization.py
│   ├── test_generation.py
│   └── conftest.py
│
├── requirements.txt
├── .env
└── README.md
```

## Endpoints Disponibles

### Health Check
`GET /v1.0/llm/health`

### Models
`GET /v1.0/llm/models` - Get Available LLM Models
`DELETE /v1.0/llm/models/{model_id}` - Remove LLM Model

### Generation
`POST /v1.0/llm/generate-response` - Generate Response
`POST /v1.0/llm/generate-llama-response` - Generate Response (Llama)

### Analysis
`POST /v1.0/llm/analyze-sentiment` - Analyze Sentiment
`POST /v1.0/llm/contextualize` - Contextualize Response
`POST /v1.0/llm/customize-response` - Customize LLM Response
`POST /v1.0/llm/evaluate` - Evaluate LLM Performance

### Training
`POST /v1.0/llm/train` - Train LLM Model

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`

## Configuración

1. Copiar el archivo .env.example a .env
2. Configurar las variables de entorno necesarias

## Ejecución

```bash
uvicorn app.main:app --reload
```

## Base URL
https://llm.csp-dev.cognitionhq.com/

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)


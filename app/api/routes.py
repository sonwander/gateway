from fastapi import APIRouter
from app.api.endpoints import llm

router = APIRouter()
router.include_router(llm.router, prefix="", tags=["llm"])

from fastapi import APIRouter
from .air_astana import router as astana_router

api_router = APIRouter()

api_router.include_router(astana_router, prefix="/airastana")
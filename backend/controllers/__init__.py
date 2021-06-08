from fastapi import APIRouter
from .air_astana import router as astana_router
from .root import router as root_router

api_router = APIRouter()
static_router = APIRouter()

api_router.include_router(astana_router, prefix="/airastana")
static_router.include_router(root_router)
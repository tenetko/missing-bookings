from fastapi import APIRouter
from .air_astana import router as astana_router
from .esky import router as esky_router
from .root import router as root_router

api_router = APIRouter()
static_router = APIRouter()

api_router.include_router(astana_router, prefix="/airastana")
api_router.include_router(esky_router, prefix="/esky")
static_router.include_router(root_router)
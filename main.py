from controllers import api_router
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, ValidationError
from typing import Union
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)

app = FastAPI(title="Missing Bookings Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {await request.form()}\n\n{exc}")
    return await request_validation_exception_handler(request, exc)
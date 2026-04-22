from fastapi import FastAPI

from app.api.endpoints.ping_endpoint import router as ping_router

def init_router(app: FastAPI) -> FastAPI:
    app.include_router(ping_router, prefix="/ping", tags=["Ping endpoint"])

    return app
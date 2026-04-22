from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import init_router

app = FastAPI(redirected_slashed=False)
app = init_router(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1",
        "http://192.168.100.54"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
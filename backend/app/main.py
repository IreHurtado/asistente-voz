import sys
import os

# *** Fix para importar app correctamente ***
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.voice import router as voice_router

app = FastAPI(title="Voice Assistant API (PRO)")

# *** CORS ***
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes restringirlo luego
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice_router)

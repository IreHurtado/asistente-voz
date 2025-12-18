import os
from dotenv import load_dotenv

load_dotenv()

APP_DIR = os.path.dirname(os.path.dirname(__file__))     # backend/app
BASE_DIR = os.path.dirname(APP_DIR)                      # backend

DATA_DIR = os.path.join(APP_DIR, "data")                 # backend/app/data

DB_PATH = os.path.join(DATA_DIR, "faqs.db")
FAISS_DIR = os.path.join(DATA_DIR, "faiss_index")
FAISS_INDEX_PATH = os.path.join(FAISS_DIR, "index.faiss")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

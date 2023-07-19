import os

from dotenv import load_dotenv

load_dotenv()

QDRANT_PATH = os.getenv("QDRANT_PATH")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

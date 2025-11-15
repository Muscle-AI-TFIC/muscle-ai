import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

class Config:
    GEMINI_MODEL = "gemini-2.5-pro"
    SUPABASE_URL = None
    SUPABASE_KEY = None
    GEMINI_API_KEY = None
    GEMINI_MODEL_INSTANCE = None

def config():
    load_dotenv()

    Config.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not Config.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found in .env")

    genai.configure(api_key=Config.GEMINI_API_KEY)
    Config.GEMINI_MODEL_INSTANCE = genai.GenerativeModel(Config.GEMINI_MODEL)

    current = os.path.abspath(__file__)
    core_dir = os.path.dirname(current)
    muscle_ai_dir = os.path.dirname(core_dir)
    src_dir = os.path.dirname(muscle_ai_dir)
    project_root = os.path.dirname(src_dir)
    cred_path = os.path.join(project_root, "key.json")

    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"key.json not found at {cred_path}")

    with open(cred_path, "r", encoding="utf-8") as f:
        keys = json.load(f)

    Config.SUPABASE_URL = keys["SUPABASE_URL"]
    Config.SUPABASE_KEY = keys["SUPABASE_KEY"]

    print("CONFIG LOADED SUCCESSFULLY")

    return Config

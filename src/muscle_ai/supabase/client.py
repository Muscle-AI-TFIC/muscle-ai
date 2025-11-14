from supabase import create_client, Client
from muscle_ai.core.config import Config

def get_supabase():
    supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
    print("Supabase initialized successfully.")
    return supabase

import os
from pathlib import Path
import streamlit as st
from supabase import create_client, Client

# Attempt to load .env from either app directory or root directory
try:
    from dotenv import load_dotenv
    app_dir = Path(__file__).resolve().parent.parent.parent
    root_dir = app_dir.parent

    possible_envs = [
        app_dir / ".env",
        root_dir / ".env",
        Path.cwd() / ".env",
    ]
    for env_path in possible_envs:
        if env_path.exists():
            load_dotenv(env_path, override=True)
            val = os.getenv("SUPABASE_URL", "")
            if val and "your-project" not in val:
                break
except ImportError:
    pass


def get_config_val(key: str, default: str = "") -> str:
    """Retrieve configuration from environment variable (.env) or Streamlit secrets."""
    val = os.getenv(key)
    if val:
        return val.strip()
    try:
        if key in st.secrets:
            return str(st.secrets[key]).strip()
    except Exception:
        pass
    return default


def clean_supabase_url(url: str) -> str:
    url = url.strip()
    if url.endswith("/rest/v1/"):
        url = url[:-len("/rest/v1/")].rstrip("/")
    elif url.endswith("/rest/v1"):
        url = url[:-len("/rest/v1")].rstrip("/")
    return url.rstrip("/")


SUPABASE_URL = clean_supabase_url(get_config_val("SUPABASE_URL"))
SUPABASE_KEY = get_config_val("SUPABASE_KEY")


def is_supabase_configured() -> bool:
    """Check if valid Supabase credentials have been provided."""
    if not SUPABASE_URL or not SUPABASE_KEY:
        return False
    if "your-project" in SUPABASE_URL or "your-supabase" in SUPABASE_KEY:
        return False
    return True


supabase: Client = None

try:
    url = SUPABASE_URL if SUPABASE_URL else "https://placeholder.supabase.co"
    key = SUPABASE_KEY if SUPABASE_KEY else "placeholder-key"
    supabase = create_client(url, key)
except Exception as e:
    supabase = None
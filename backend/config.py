import os
from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv

# Auto-load .env from project root if it exists
env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

def _load_groq_keys() -> list:
    keys_env = os.getenv("GROQ_API_KEYS", "")
    single_key = os.getenv("GROQ_API_KEY", "")
    keys = [k.strip() for k in keys_env.split(",") if k.strip()]
    if single_key.strip() and single_key.strip() not in keys:
        keys.append(single_key.strip())
    return keys

class Settings(BaseModel):
    PROJECT_NAME: str = "CampusQuant AI"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # Secret Key for JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "campusquant_secret_key_default_jwt_token_auth")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", str(60 * 24))) # 24 hours
    
    # Database Settings (XAMPP MySQL on localhost:3306, with SQLite fallback)
    MYSQL_DB_URL: str = os.getenv("MYSQL_DB_URL", "mysql+pymysql://root:@localhost:3306/campusquant_db")
    SQLITE_DB_URL: str = os.getenv("SQLITE_DB_URL", "sqlite:///./campusquant.db")
    
    # Groq API Keys Pool (Rotating keys loaded dynamically from environment variables)
    GROQ_API_KEYS: list = _load_groq_keys()
    
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    GROQ_FALLBACK_MODEL: str = os.getenv("GROQ_FALLBACK_MODEL", "mixtral-8x7b-32768")

    # SMTP Gmail Email Credentials
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_EMAIL: str = os.getenv("SMTP_EMAIL", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")

settings = Settings()

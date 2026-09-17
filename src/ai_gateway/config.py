from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GROQ_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    CHATGPT_MINI_API_KEY: str | None = None
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    
    # This ONE line replaces load_dotenv and os.getenv entirely!
    model_config = SettingsConfigDict(env_file=".env")

# Pydantic automatically reads the .env file and fills these in wed on't have to pass them manually!
settings = Settings()

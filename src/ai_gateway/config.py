from pydantic_settings import BaseSettings, SettingsConfigDict
'''is a class is inherited from the BaseSetting it is automatically
reads and get the values from the .env file(locally and 
in production from the OS because in production it is not stored in 
.env but rather in the OS as environmenment varables)'''

class Settings(BaseSettings):
    GROQ_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    CHATGPT_MINI_API_KEY: str | None = None
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    
    # This ONE line replaces load_dotenv and os.getenv entirely!
    model_config = SettingsConfigDict(
            env_file=".env",
            env_prefix="",
            extra="ignore",
        )
# Pydantic automatically reads the .env file and fills these in wed on't have to pass them manually!
settings = Settings()

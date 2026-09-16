"""import os

from dotenv import load_dotenv

load_dotenv()

print(os.getenv("MY_KEYS"))

THIS IS A SIMPLE TEST TO CHECK AND SEE HOW TO GET THE KEYS FROMT HE .ENV FILE
"""

import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
'''Building a validation for the keys retrival so that there is strcit keys placement and other thins in the 
env file'''
class Settings(BaseModel):
    GROQ_API_KEY :str
    GEMINI_API_KEY= str
    CHATGPT_MINI_API_KEY: str
    HOST : str = '0.0.0.0'
    PORT: int = 8000


# this is a singleton way a api can be exposed hence 
settings = Settings(
    GROQ_API_KEY= os.getenv("GROQ_API_KEY"),
    GEMINI_API_KEY= os.getenv("GEMINI_API_KEY"),
    CHATGPT_API_KEY= os.getenv("CHATGPT_API_KEY"),
    HOST=os.getenv("HOST", "0.0.0.0"),#host is like the address of the server
    PORT=int(os.getenv("PORT",'8000'))#port is the entry point a way to direct a user at out application
)
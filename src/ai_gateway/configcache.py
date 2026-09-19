'''through this the cache config required variables from the 
.env file will be taken '''

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class CacheSettings(BaseSettings):
    '''this class reads the cache variables from the 
    env file and also good for validation'''

    ENABLE_CACHE: bool = Field(
        default = True,
        description = "if False the gateway will bypass the cache entirely"
    )

    CACHE_TTL_HOURS: int = Field(
        default = 24,
        description = "how long a memory will be cached"
    )

    CACHE_BACKEND: str = Field(
        default = 'memory',
        description = "the backend used for caching redis or memory"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
    )



cache_settings = CacheSettings()










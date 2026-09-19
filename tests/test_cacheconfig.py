from ai_gateway.configcache import CacheSettings



def test_defaults():
    settings = CacheSettings()
    assert settings.ENABLE_CACHE is True
    assert settings.CACHE_TTL_HOURS == 24
    assert settings.CACHE_BACKEND == "memory"
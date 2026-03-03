import hashlib, json

class CacheService:
    def __init__(self):
        self._cache = {}

    def make_key(self):
        if isinstance(data, dict):
            data = json.dumps(data, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()
    
    def get(self, data):
        key = self.make_key(data)
        return self.cache_get(key)
    
    def set(self, data, value):
        key = self.make_key(data)
        self._cache[key] = value
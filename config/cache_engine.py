from typing import Optional
import time
import json

# This is a Custom method for updating the cache with the results from the database.


class Cache():
    def __init__(self):
        self.memory = {}
    # I created a custom method to get records from the RAM cache for speed

    def get_cache(self, key: str) -> Optional[str]:
        try:
            cache_item = self.memory.get(key)
            if (cache_item):
                value, expiration_time = cache_item
                if time.time() > expiration_time:
                    print(f"Cache Expired for key {key}")
                    del self.memory[key]
                    return None
                else:
                    return json.loads(value)
            return None
        except Exception as e:
            print(
                f"an exception occured while getting the cache for key: {key}")
            return None

    # The default time for the object to last in the ram cache is 30 minutes.

    def set_cache(self, key: str, value, ttl: int = 1800):
        try:
            if isinstance(value, (list, dict)):
                value = json.dumps(value)

                expiration_time = time.time() + ttl

                self.memory[key] = (value, expiration_time)
        except Exception as e:
            print(f"Error occurred while setting cache for key {key}: {e}")

    def clear_cache(self, key: str):
        try:
            if key in self.memory:
                del self.memory[key]
                print(f"Cache cleared for the key {key}")
            else:
                print(f"No cache record found for key {key}")
        except Exception as e:
            print(f"Error occurred while clearing cache for key {key}: {e}")

    def clear_expired(self):
        try:
            current_time = time.time()
            expired_keys = [key for key, (value, expiration) in self.memory.items(
            ) if current_time > expiration]
            for key in expired_keys:
                del self.memory[key]
            print(f"Expired cache items cleared: {expired_keys}")
        except Exception as e:
            print(f"Error occurred while clearing expired cache items: {e}")

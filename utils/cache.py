import redis
import json
from typing import Optional
from utils.logger import Logger

logger = Logger()
component_name = "redis"


def create_redis() -> redis.ConnectionPool:
    try:
        return redis.ConnectionPool(
            host='0.0.0.0',
            port=6379,
            db=0,
            decode_responses=True
        )
    except Exception as e:
        logger.err(component_name,
                   f"Error occurred while creating Redis connection pool: {e}")


pool = create_redis()


def get_redis() -> redis.Redis:
    try:
        # Get a connection from the pool
        return redis.Redis(connection_pool=pool)
    except Exception as e:
        logger.err(component_name,
                   f"Error occurred while getting Redis client: {e}")
        raise e


cache = get_redis()


def get_cache(key: str) -> Optional[str]:
    try:
        logger.log(component_name, f"Getting value for key: {key}")
        return cache.get(key)
    except Exception as e:
        logger.log(component_name,
                   f"Error occured while getting cache for key {key}. Error -> {e}")
        return None


def set_cache(key: str, value, expire: int = 30) -> Optional[str]:
    try:
        logger.log(component_name, f"Setting value for key: {
                   key} with expiration: {expire} seconds")
        if isinstance(value, (list, dict)):
            value = json.dumps(value)
        cache.set(key, value, ex=expire)
    except Exception as e:
        logger.err(component_name,
                   f"Error occured while getting cache for key {e}")

import os
from dotenv import load_dotenv
import redis

load_dotenv()


class Base:
    def __init__(self, service):
        if service == "verifyMailService":
            db = 10
        else:
            raise Exception("Not Implemented")
        self._redis_url = os.getenv("BROKER") + f"/{db}"
        self._db: redis.Redis = redis.Redis.from_url(self._redis_url)

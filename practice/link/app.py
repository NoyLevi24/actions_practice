import os, redis
host = os.getenv("REDIS_HOST", "cache")
port = int(os.getenv("REDIS_PORT", "6379"))
r = redis.Redis(host=host, port=port)
print("PING:", r.ping())

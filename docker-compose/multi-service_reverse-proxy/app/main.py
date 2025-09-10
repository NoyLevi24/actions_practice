from flask import Flask
import os
import redis

app = Flask(__name__)


def get_redis_client() -> redis.Redis:
    redis_host = os.getenv("REDIS_HOST", "redis")
    redis_port = int(os.getenv("REDIS_PORT", "6379"))
    return redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


redis_client = get_redis_client()


@app.route("/")
def index():
    visits = redis_client.incr("visits")
    return f"Hello from Flask via Nginx! Visits: {visits}\n"

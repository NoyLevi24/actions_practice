FROM python:3.11-alpine
WORKDIR /app
RUN pip install --no-cache-dir redis
COPY app.py .
ENV REDIS_HOST=cache REDIS_PORT=6379
CMD ["python", "app.py"]

FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

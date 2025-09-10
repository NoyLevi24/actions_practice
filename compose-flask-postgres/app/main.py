from flask import Flask, jsonify, request
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        dbname=os.getenv("POSTGRES_DB", "appdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "apppassword"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        cursor_factory=RealDictCursor,
    )
    return connection


@app.route("/")
def index():
    return jsonify({"message": "Flask + Postgres is running"})


@app.route("/items", methods=["GET"]) 
def list_items():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM items ORDER BY id ASC;")
            rows = cur.fetchall()
            return jsonify(rows)


@app.route("/items", methods=["POST"]) 
def create_item():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return jsonify({"error": "name is required"}), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO items (name) VALUES (%s) RETURNING id, name;", (name,))
            row = cur.fetchone()
            conn.commit()
            return jsonify(row), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))


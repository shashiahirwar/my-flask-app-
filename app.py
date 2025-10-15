from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def hello():
    name = os.getenv("APP_NAME", "World")
    return jsonify(message=f"Hello, {name}!", status="ok")

@app.get("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    # Only used when running locally with `python app.py`
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)


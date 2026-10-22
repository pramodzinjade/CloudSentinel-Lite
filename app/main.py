from flask import Flask, jsonify
from datetime import datetime, timezone
import os

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>my CloudSentinel Lite by pramod on docker container</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
                padding: 80px 20px;
            }
            .card {
                max-width: 600px;
                margin: auto;
                padding: 35px;
                background: #1e293b;
                border-radius: 15px;
            }
            h1 { color: #38bdf8; }
            .status { color: #4ade80; }
            a { color: #38bdf8; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CloudSentinel Lite</h1>
            <h2 class="status">● Application Running</h2>
            <p>Your cloud deployment is working successfully.</p>
            <p>Powered by Python, Flask, Docker and AWS EC2.</p>
            <p><a href="/health">Health Check</a></p>
            <p><a href="/api/info">Application Information</a></p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "project": "CloudSentinel-Lite",
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "application": "CloudSentinel-Lite",
        "version": "2.0",
        "environment": os.getenv("ENV", "development"),
        "status": "running"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
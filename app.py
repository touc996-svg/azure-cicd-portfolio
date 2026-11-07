import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Azure CI/CD Portfolio</title>
      <style>
        body { font-family: Arial; background: #f1f5f9; padding: 50px; }
        main { max-width: 700px; margin: auto; background: white;
               padding: 35px; border-radius: 14px; }
        h1 { color: #0078d4; }
        .status { background: #e8f7ed; padding: 15px; border-radius: 8px; }
      </style>
    </head>
    <body>
      <main>
        <h1>Azure CI/CD Portfolio</h1>
        <div class="status">Application status: Operational</div>
        <p>Environment: """ + os.getenv("APP_ENV", "development") + """</p>
        <p>Version: """ + os.getenv("APP_VERSION", "1.0.0") + """</p>
        <p><a href="/health">Health check</a></p>
        <p><a href="/api/status">Application API</a></p>
      </main>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/api/status")
def status():
    return jsonify({
        "project": "Azure CI/CD Portfolio",
        "status": "operational",
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))

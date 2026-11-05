import werkzeug
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "2.3.7"

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Aplicación de ejemplo para gestión de dependencias"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "proyecto-dependencias",
        "framework": "Flask 2.3.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

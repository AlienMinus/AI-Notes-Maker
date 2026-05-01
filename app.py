import os

# Suppress TensorFlow oneDNN warning and C++ info logs
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve

from summarizer import generate_summary
from notes_generator import generate_notes
from keywords import extract_keywords
from mindmap_generator import generate_mindmap

app = Flask(__name__)

# CORS
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API running 🚀"})

# 🔹 Summarizer
@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json() or {}
    text = data.get("text", "")
    
    if not text.strip():
        return jsonify({"error": "Empty text"})

    return jsonify({
        "summary": generate_summary(text)
    })

# 🔹 Notes
@app.route("/notes", methods=["POST"])
def notes():
    data = request.get_json() or {}
    text = data.get("text", "")
    
    if not text.strip():
        return jsonify({"error": "Empty text"})

    return jsonify({
        "notes": generate_notes(text)
    })

# 🔹 Keywords
@app.route("/keywords", methods=["POST"])
def keywords():
    data = request.get_json() or {}
    text = data.get("text", "")
    
    if not text.strip():
        return jsonify({"error": "Empty text"})

    return jsonify({
        "keywords": extract_keywords(text)
    })

# 🔹 Mindmap
@app.route("/mindmap", methods=["POST"])
def mindmap():
    data = request.get_json() or {}
    text = data.get("text", "")
    
    if not text.strip():
        return jsonify({"error": "Empty text"})

    return jsonify(generate_mindmap(text))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Server running on port {port} 🚀")
    serve(app, host="0.0.0.0", port=port)
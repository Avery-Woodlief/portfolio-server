from flask import Flask, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app, origins=["https://avery-woodlief.github.io/portfolio/"])

@app.route("/repos")
def repos():
    token = os.getenv("GITHUB_TOKEN")

    response = requests.get(
        "https://api.github.com/users/Avery-Woodlief/repos",
        headers={
            "Authorization": f"Bearer {token.strip()}"
        }
    )

    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True, port=5000)

import os

import openai
import flask

app = flask.Flask(__name__)
api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
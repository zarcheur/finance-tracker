from flask import Flask, render_template, request, jsonify
from nlp_parser import parse_expense
from sheety_handler import post_to_sheety

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/parse", methods=["POST"])
def parse():
    data = request.get_json()
    user_input = data.get("text", "")
    result = parse_expense(user_input)
    return jsonify(result)

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json()
    response = post_to_sheety(data)
    return jsonify({"status": "success", "response": response})

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
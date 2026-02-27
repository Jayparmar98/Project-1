from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({
        "text": text,
        "sentiment": sentiment,
        "polarity": round(polarity, 2),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
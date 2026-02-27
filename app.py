from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    return "NLP Sentiment Analyzer Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

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
        "polarity": polarity
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
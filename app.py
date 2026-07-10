from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


def analyze_sentiment(text):
    analysis = TextBlob(text)

    polarity = round(analysis.sentiment.polarity, 3)
    subjectivity = round(analysis.sentiment.subjectivity, 3)

    if polarity > 0:
        sentiment = "Positive"
        emoji = "😊"
        css_class = "positive"
    elif polarity < 0:
        sentiment = "Negative"
        emoji = "😞"
        css_class = "negative"
    else:
        sentiment = "Neutral"
        emoji = "😐"
        css_class = "neutral"

    return sentiment, polarity, subjectivity, emoji, css_class


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("user_text", "").strip()

        if not user_text:
            error = "Please enter some text before analyzing."
        else:
            sentiment, polarity, subjectivity, emoji, css_class = analyze_sentiment(
                user_text
            )

            result = {
                "sentiment": sentiment,
                "polarity": polarity,
                "subjectivity": subjectivity,
                "emoji": emoji,
                "css_class": css_class,
            }

    return render_template(
        "index.html",
        result=result,
        error=error,
        user_text=user_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

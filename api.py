from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

pipeline = joblib.load("spam_filter.pkl")

@app.get("/")
def home():
    return jsonify({
        "message": "Spam Filter API is running",
        "endpoint": "/detect",
        "method": "POST"
    })

@app.post("/detect")
def detect():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Missing JSON payload"
        }), 400

    subject = data.get("subject", "").strip()
    mail_content = data.get("mail_content", "").strip()

    if not subject and not mail_content:
        return jsonify({
            "error": "Subject or mail_content is required"
        }), 400

    text = f"Subject: {subject}\r\n{mail_content}"

    prediction = pipeline.predict([text])[0]
    probs = pipeline.predict_proba([text])[0]

    return jsonify({
        "prediction": "spam" if prediction == 1 else "ham",
        "ham_probability": round(float(probs[0]), 4),
        "spam_probability": round(float(probs[1]), 4)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3100, debug=True)
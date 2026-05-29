# Spam Filter API

A Machine Learning powered REST API for email spam detection built using Flask and Scikit-Learn.

The API analyzes email subject and content, then predicts whether the email is **Spam** or **Ham (Legitimate Email)** while also returning confidence probabilities.

## Live API

**Base URL**

https://spam-filter-7x06.onrender.com

---

## Features

* Spam/Ham email classification
* RESTful API
* Probability scores for both classes
* Trained using Scikit-Learn
* Lightweight and fast inference
* Deployable on Render, Railway, AWS, VPS, or Docker

---

## Tech Stack

* Python
* Flask
* Scikit-Learn
* TF-IDF Vectorization
* Logistic Regression
* Joblib

---

## API Endpoint

### Detect Spam

**Endpoint**

```http
POST /detect
```

### Request Body

```json
{
    "subject": "Congratulations!",
    "mail_content": "You have won a free iPhone. Click here to claim."
}
```

### Success Response

```json
{
    "prediction": "spam",
    "ham_probability": 0.0435,
    "spam_probability": 0.9565
}
```

### Error Response

```json
{
    "error": "Missing JSON payload"
}
```

or

```json
{
    "error": "Subject or mail_content is required"
}
```

---

## Example cURL Request

```bash
curl -X POST https://spam-filter-7x06.onrender.com/detect \
-H "Content-Type: application/json" \
-d '{
    "subject":"Congratulations!",
    "mail_content":"You have won a free iPhone. Click here to claim."
}'
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/manodhithyaa-dev/spam_filter.git

cd spam_filter
```

### Create Virtual Environment

```bash
python -m venv ai-env
```

Linux/macOS:

```bash
source ai-env/bin/activate
```

Windows:

```bash
ai-env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python api.py
```

Server starts on:

```text
http://localhost:3100
```

---

## Model Information

The model is trained using:

* TF-IDF Vectorization
* Logistic Regression Classifier
* Email Subject + Email Body Features

Input text is transformed into the format:

```text
Subject: <email_subject>
<email_content>
```

before prediction.

---

## Project Structure

```text
spam_filter/
│
├── api.py
├── spam_filter.pkl
├── requirements.txt
├── Procfile
├── spam.ipynb
│
└── dataset/
    └── spam_ham_dataset.csv
```

---

## Future Improvements

* Phishing Email Detection
* URL Reputation Analysis
* Attachment Risk Analysis
* Email Header Analysis
* Multi-class Classification
* Explainable AI Predictions

---

## Author

Manodhithyaa C S

GitHub:
https://github.com/manodhithyaa-dev

# Spam Filter API

A Machine Learning powered REST API that detects whether an email is **Spam** or **Ham (Legitimate Email)** using a TF-IDF + Logistic Regression pipeline built with Flask and Scikit-Learn.

The API accepts an email subject and email content, then returns a classification along with confidence scores.

---

## Live API

**Base URL**

```text
https://spam-filter-7x06.onrender.com
```

### Interactive Playground

Test the API directly from your browser:

```text
https://spam-filter-7x06.onrender.com/tryit
```

---

## Features

* Spam/Ham email classification
* RESTful JSON API
* Confidence probability scores
* Fast inference
* Lightweight deployment
* Interactive API testing page
* Easy integration into web and mobile applications

---

## Tech Stack

* Python
* Flask
* Scikit-Learn
* TF-IDF Vectorization
* Logistic Regression
* Joblib

---

## API Reference

### Detect Spam

**Endpoint**

```http
POST /detect
```

### Request Headers

```http
Content-Type: application/json
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

## Example Python Request

```python
import requests

response = requests.post(
    "https://spam-filter-7x06.onrender.com/detect",
    json={
        "subject": "Congratulations!",
        "mail_content": "You have won a free iPhone. Click here to claim."
    }
)

print(response.json())
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

The classifier is trained using:

* TF-IDF Vectorization
* Logistic Regression
* Email Subject + Email Body Features

Input is transformed into:

```text
Subject: <email_subject>
<email_content>
```

before being passed to the model.

---

## Project Structure

```text
spam_filter/
│
├── api.py
├── spam_filter.pkl
├── requirements.txt
├── README.md
├── spam.ipynb
│
├── dataset/
│   └── spam_ham_dataset.csv
│
└── templates/
    ├── readme.html
    └── tryit.html
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

**Manodhithyaa C S**
### Portfolio
```
https://manodhithyaa.me/
```
### GitHub
```
https://github.com/manodhithyaa-dev
```
### Repository
```
https://github.com/manodhithyaa-dev/spam_filter
```

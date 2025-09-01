# Sentiment Analysis with Django

This project is a simple web application built with **Django** and **scikit-learn** that performs sentiment analysis on user input text. It classifies text as **positive** or **negative**.

---

## Features
- Django-based web interface
- Machine Learning model trained with scikit-learn
- Naive Bayes classifier for sentiment detection
- Pre-trained model saved with joblib (`sentiment_model.pkl`, `vectorizer.pkl`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/marjanrezaei/sentiment-analysis-django.git
   cd sentiment-analysis-django
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Train the model (optional, if you want to regenerate it):

bash
Copy code
python train_model.py
Usage
Run migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Open in browser:

cpp
Copy code
http://127.0.0.1:8000/
Enter text in the input box, and the app will classify it as positive or negative.

Project Structure
bash
Copy code
sentiment-analysis-django/
│── ml/                     # Machine Learning logic
│── templates/              # HTML templates
│── sentiment_model.pkl     # Saved ML model
│── vectorizer.pkl          # Saved vectorizer
│── train_model.py          # Script to train model
│── manage.py
│── requirements.txt
│── README.md
Contributing
Feel free to fork this repository, make improvements, and submit a pull request.

License
This project is licensed under the MIT License.
# Sentiment Analysis Web App

A web application built with Django that takes user input text and predicts its sentiment (positive or negative) using an AI model.

## Technologies
- Python
- Django
- Scikit-learn
- Pandas, NumPy
- Git / GitHub
- Render (for online deployment)
- Docker (optional)

## Features
- Takes text input from the user and analyzes sentiment
- Predicts whether the text is positive or negative
- Integrated into a Django web application
- Online deployment for direct use

## Installation / Setup

1. Clone the repository:
```bash
git clone <GitHub repository link>
cd sentiment-analysis-django
Install required packages:

bash
Copy code
pip install -r requirements.txt
Run the Django server:

bash
Copy code
python manage.py runserver
Open your browser and go to:

arduino
Copy code
http://127.0.0.1:8000/sentiment/
Dataset and AI Model
Suggested dataset: IMDb Movie Reviews (50k movie reviews)

AI model: Multinomial Naive Bayes using Scikit-learn

Model files: sentiment_model.pkl and vectorizer.pkl

Author
Marjan Rezaei

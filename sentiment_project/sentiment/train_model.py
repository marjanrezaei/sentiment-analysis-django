import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample dataset (you can replace it with a larger dataset)
data = {
    "text": [
        "I love this product",
        "This is amazing",
        "I hate this service",
        "This is terrible"
    ],
    "label": [1, 1, 0, 0]  # 1 = Positive, 0 = Negative
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Save the trained model and vectorizer
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and Vectorizer saved successfully!")

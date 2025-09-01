import os
import joblib
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# فقط وقتی فایل وجود دارد بارگذاری کن
if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
else:
    model = None
    vectorizer = None

def predict_sentiment(request):
    if request.method == "POST" and model is not None:
        text = request.POST.get("text")
        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)[0]
        sentiment = "positive" if prediction == 1 else "negative"
        return render(request, "result.html", {"prediction": sentiment, "text": text})
    return render(request, "index.html")

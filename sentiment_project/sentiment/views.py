import joblib
from django.shortcuts import render

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_sentiment(request):
    if request.method == "POST":
        text = request.POST.get("text")
        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)[0]
        return render(request, "result.html", {"prediction": prediction})
    return render(request, "index.html")

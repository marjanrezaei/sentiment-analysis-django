from django.urls import path, include

urlpatterns = [
    path('sentiment/', include('sentiment.urls')),
]
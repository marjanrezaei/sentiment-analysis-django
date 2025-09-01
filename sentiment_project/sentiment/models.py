from django.db import models

# Example model if you want to store user reviews
class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True)  # 'positive' or 'negative'

    def __str__(self):
        return self.text[:50]  

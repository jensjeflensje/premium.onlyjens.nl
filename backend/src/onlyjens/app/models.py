from django.db import models

class Payment(models.Model):
    message = models.TextField(blank=True)
    author = models.TextField(blank=True)
    amount = models.FloatField()
    stripe_id = models.TextField()
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

from django.db import models

class Payment(models.Model):
    message = models.TextField(blank=True)
    author = models.TextField(blank=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

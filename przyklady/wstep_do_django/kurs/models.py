from django.db import models

# Create your models here.

class Szkolenie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    szkolenie_data = models.DateTimeField()
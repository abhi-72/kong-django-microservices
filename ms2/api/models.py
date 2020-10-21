from django.db import models

class Bird(models.Model):
    name = models.CharField(max_length=30)

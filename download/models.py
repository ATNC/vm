from django.db import models

class Title(models.Model):
    name = models.CharField(max_length=255)
# Create your models here.

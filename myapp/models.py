from django.db import models

# Create your models here.

class Shows(models.Model):
    banda = models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    data = models.DateField()


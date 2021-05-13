from django.db import models


class Reciepe(models.Model):
    reciepe_name = models.CharField(max_length=100)
    ingridiants = models.TextField()
    process = models.TextField()
    images = models.ImageField(upload_to='media/')




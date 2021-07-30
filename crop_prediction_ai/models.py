from django.db import models
from django.contrib.auth.models import User

class advertisement(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    cost = models.IntegerField()
    image = models.ImageField(upload_to='crop\images')
    address = models.CharField(max_length=5000)
    currency = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

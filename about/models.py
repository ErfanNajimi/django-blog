from django.db import models

# Create your models here.
class About(models):
    title = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
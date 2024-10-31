from django.db import models

# Create your models here.
class Skills(models.Model):
    emailid = models.CharField(max_length=250)
    skills = models.TextField()
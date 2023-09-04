from django.db import models
# Create your models here.

class Info(models.Model):
    peoplenums = models.CharField(max_length=10,default='')
    jobs = models.CharField(max_length=10,default='')
    locations = models.CharField(max_length=10,default='')
    ages = models.CharField(max_length=10,default='')

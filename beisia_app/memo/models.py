from django.db import models

class Lists(models.Model):
    date = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    lists = models.TextField()
    
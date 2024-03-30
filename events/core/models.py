from django.db import models

# Create your models here.
class News1(models.Model):
    period = models.CharField(max_length=32)
    title = models.TextField(max_length=128, null=True, blank=True)
    text = models.TextField(max_length=65536, null=True, blank=True)

class News2(models.Model):
    period = models.CharField(max_length=32)
    title = models.TextField(max_length=128, null=True, blank=True)
    text = models.TextField(max_length=65536, null=True, blank=True)

class News3(models.Model):
    period = models.CharField(max_length=32)
    title = models.TextField(max_length=128, null=True, blank=True)
    text = models.TextField(max_length=65536, null=True, blank=True)
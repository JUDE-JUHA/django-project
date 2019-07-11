from django.db import models


# Create your models here.

class Works(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')


class Document(models.Model):
    desc = models.TextField(max_length=500)
    pdf = models.FileField(upload_to='pdf')

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    msg = models.TextField(max_length=350)

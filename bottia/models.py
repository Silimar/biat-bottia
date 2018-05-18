from django.db import models


class Intents(models.Model):
    text = models.CharField(max_length=50)


class Response(models.Model):
    text = models.CharField(max_length=600)
    Intents = models.ForeignKey(Intents, on_delete=models.CASCADE, default=None)


class Message(models.Model):
    text = models.CharField(max_length=600)
    Intents = models.ForeignKey(Intents, on_delete=models.CASCADE, default=None)


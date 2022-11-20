from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Phrases(models.Model):
    phrase = models.CharField(max_length=600)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return self.phrase

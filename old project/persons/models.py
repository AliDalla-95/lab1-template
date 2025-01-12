from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    work = models.CharField(max_length=100)

    def __str__(self):
        return self.name

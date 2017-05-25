from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    family = models.ForeignKey(User, on_delete=models.CASCADE)
    is_missing = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Witness(models.Model):
    target = models.ForeignKey(Person, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=10000)

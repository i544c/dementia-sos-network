from django.db import models
from django.contrib.auth.models import User

class Aged(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    family = models.ForeignKey(User, on_delete=models.CASCADE)
    is_missing = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

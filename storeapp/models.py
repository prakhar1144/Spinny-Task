from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Box(models.Model):
    length = models.IntegerField()
    breadth = models.IntegerField()
    height = models.IntegerField()

    creator = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    @property
    def area(self):
        return self.length * self.breadth

    @property
    def volume(self):
        return self.length * self.breadth * self.height

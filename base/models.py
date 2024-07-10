from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Category(models.Model):
    picture = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading


class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    content = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET("Category is undefined"))

    def __str__(self):
        return f"{self.category} _ {self.name}"


class User(AbstractUser):
    topics = models.ManyToManyField(Topic, related_name='topics', blank=True)
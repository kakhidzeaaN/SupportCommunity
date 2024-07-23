from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# picture = models.ImageField(null=True, blank=True)


class Category(models.Model):
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading


class Topic(models.Model):
    picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    content = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET("Category is undefined"))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.category} _ {self.name}"


class Conversation(models.Model):
    type = models.CharField(max_length=70)

    def __str__(self):
        return self.type


class Meeting(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown Creator"))
    title = models.CharField(max_length=100)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    topic = models.ManyToManyField(Topic, related_name='Topic', blank=True)
    category = models.ManyToManyField(Category, related_name='Category', blank=True)
    file = models.FileField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title", 'created']

    def __str__(self):
        return f"{self.title}"


class User(AbstractUser):
    topics = models.ManyToManyField(Topic, related_name='topics', blank=True)
    meetings = models.ManyToManyField(Meeting, related_name='meetings', blank=True)
    avatar = models.ImageField(null=True, default='avatar.png')
    bio = models.TextField(null=True)

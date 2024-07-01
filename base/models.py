from django.db import models


# Create your models here.
class Topics(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    content = models.CharField(max_length=200)
    group = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.group} _ {self.name}"


# family: parenting, pregnancy, woman, man
# Health: depression, chronic illness, anxiety
# Other: addiction, sleep, grief and loss
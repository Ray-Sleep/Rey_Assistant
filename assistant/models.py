from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    number = models.BigIntegerField()
    email = models.EmailField(default=None,null=True)
    password = models.CharField(max_length=64)

from django.db import models
from accounts.models import User

# Create your models here.


class ProfileUpdate(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class CreateBid(models.Model):
    uni = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_value = models.CharField(max_length=30)
    bid_time = models.CharField(max_length=30)

    def __str__(self):
        return self.bid_value
from django.db import models
from accounts.models import User
from university.models import CreateBid

# Create your models here.


class CreateProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    Sub_category = models.CharField(max_length=200)
    durations = models.CharField(max_length=200)
    bidding = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FinalizeUnivercity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uni_id = models.ForeignKey(CreateBid, on_delete=models.CASCADE)
    project = models.ForeignKey(CreateProject, on_delete=models.CASCADE)

    def __str__(self):
        return self.project
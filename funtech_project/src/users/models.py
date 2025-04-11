from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    coins = models.IntegerField(default=0)

class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)


class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    execute_at = models.DateTimeField()
    is_processed = models.BooleanField(default=False)

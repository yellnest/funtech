from django.db import models
from rest_framework import serializers

from src.users.models import User, RewardLog, ScheduledReward


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'coins']
        read_only_fields = ['coins']


class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ['id', 'amount', 'given_at']


class ScheduledRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledReward
        fields = ['id', 'amount', 'execute_at']

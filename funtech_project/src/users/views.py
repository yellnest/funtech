from datetime import timedelta

from django.utils import timezone
from rest_framework import status

from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from src.users.tasks import schedule_reward_task
from src.users.models import RewardLog, ScheduledReward
from src.users.serializers import CustomUserSerializer, RewardLogSerializer, ScheduledRewardSerializer


class ProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class RewardListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RewardLogSerializer

    def get_queryset(self):
        return RewardLog.objects.filter(user=self.request.user)


class RequestRewardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # Check if user already requested reward today
        today = timezone.now().date()
        today_rewards = ScheduledReward.objects.filter(
            user=user,
            execute_at__date=today
        )

        if today_rewards.exists():
            return Response(
                {'error': 'Можно запрашивать только 1 награду в день'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create scheduled reward for 5 minutes later
        execute_at = timezone.now() + timedelta(minutes=5)
        scheduled_reward = ScheduledReward.objects.create(
            user=user,
            amount=10,
            execute_at=execute_at
        )

        # Schedule Celery task
        schedule_reward_task.apply_async(
            (scheduled_reward.id,),
            eta=execute_at
        )

        serializer = ScheduledRewardSerializer(scheduled_reward)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

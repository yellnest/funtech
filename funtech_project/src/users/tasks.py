from celery import shared_task
from django.utils import timezone

from src.users.models import ScheduledReward, RewardLog


@shared_task
def schedule_reward_task(reward_id):
    try:
        reward = ScheduledReward.objects.get(id=reward_id, is_processed=False)

        # Process reward
        user = reward.user
        user.coins += reward.amount
        user.save()

        # Create reward log
        RewardLog.objects.create(
            user=user,
            amount=reward.amount
        )

        # Mark as processed
        reward.is_processed = True
        reward.save()

        return f"Награда {reward_id} отправлена успешно"
    except ScheduledReward.DoesNotExist:
        return f"Награда {reward_id} не найдена или уже получена"
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Кастомный UserAdmin для модели User
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'coins', 'is_staff')
    list_display_links = ('id', 'username')



@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'given_at')
    list_display_links = ('id', 'user')


@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'execute_at', 'is_processed')
    list_display_links = ('id', 'user')

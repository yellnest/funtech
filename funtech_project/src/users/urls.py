from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from src.users.views import ProfileView, RewardListView, RequestRewardView

urlpatterns = [
    # Авторизация через JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Основные API
    path('profile/', ProfileView.as_view(), name='profile'),
    path('rewards/', RewardListView.as_view(), name='reward-list'),
    path('rewards/request/', RequestRewardView.as_view(), name='request-reward')
]

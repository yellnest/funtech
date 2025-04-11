from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Reward Platform API",
        default_version='v1',
        description="API for user reward system",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[JWTAuthentication],
)

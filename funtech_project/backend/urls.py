from django.contrib import admin
from django.urls import path, include

from backend.swagger_schema import schema_view

urlpatterns = [
    path('api/', include('src.users.urls')),
    path('admin/', admin.site.urls),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

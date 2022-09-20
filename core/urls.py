from django.contrib import admin
from django.urls import path, include

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
        # The whole application home is loaded once all views are loaded
    path('', views.ApiHome.as_view(), name="api-home"),
    path('ecommerce/', include('ecommerce.urls')),
    path('auth/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

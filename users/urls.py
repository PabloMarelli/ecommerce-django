from django.urls import path, include
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='users-detail'),
]

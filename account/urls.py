from django.urls import path
from .views import RegisterUserView, LoginUserView, UserDetailView

urlpatterns = [
    path('users/register/', RegisterUserView.as_view(), name='register'),
    path('users/login/', LoginUserView.as_view(), name='login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

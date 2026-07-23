from django.urls import path
from .views import RegisterView, CustomAuthToken, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', CustomAuthToken.as_view(), name='auth_login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]

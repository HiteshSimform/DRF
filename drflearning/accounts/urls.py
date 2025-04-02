from django.urls import path, include
from .views import CustomUserRegistrationView, CustomUserLoginView, CustomUserLogoutView
urlpatterns = [
    path('auth/register/',CustomUserRegistrationView.as_view(),name='user-registration'),
    path('auth/login/',CustomUserLoginView.as_view(),name='user-login'),
    path('auth/logout/',CustomUserLogoutView.as_view(),name='user-logout'),
]

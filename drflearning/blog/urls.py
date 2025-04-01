from django.urls import path
from .views import blog_list, blog_details

urlpatterns = [
    path('blogs/',blog_list),
    path('blogs/<int:pk>/',blog_details),
]

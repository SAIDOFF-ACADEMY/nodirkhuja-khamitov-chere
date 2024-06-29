from user import views
from django.urls import path

urlpatterns = [
    path('login', views.LogInView.as_view(), name='user-login'),
]   
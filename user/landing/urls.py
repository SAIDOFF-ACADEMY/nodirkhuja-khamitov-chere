from user.landing import views
from django.urls import path

urlpatterns = [
    path('create', views.UserContactApplicationCreateView.as_view(), name='user-login'),
]   
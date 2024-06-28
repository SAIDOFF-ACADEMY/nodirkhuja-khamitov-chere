from common import views
from django.urls import path

urlpatterns = [
    path('settings', views.SettingsView.as_view(), name='settings-admin'),
    path('login', views.LogInView.as_view(), name='login')
]
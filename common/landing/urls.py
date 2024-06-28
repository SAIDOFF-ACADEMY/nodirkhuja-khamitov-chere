from common.landing import views

from django.urls import path

urlpatterns = [
    path('settings', views.SettingsView.as_view(), name='settings-landing')
]
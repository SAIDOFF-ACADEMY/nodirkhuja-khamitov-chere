from common.landing import views

from django.urls import path

urlpatterns = [
    path('settings', views.SettingsView.as_view(), name='landing-settings'),
    path('page/get/<str:slug>', views.RetrievePageView.as_view(), name='landing-page-get'),
    path('gallery/list', views.ListGalleryView.as_view(), name='landing-gallery-list')
]
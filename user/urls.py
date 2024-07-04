from user import views
from django.urls import path

urlpatterns = [
    path('login', views.LogInView.as_view(), name='user-login'),
    path('list', views.UserContactApplicationListView.as_view(), name='admin-contact-list'),
    path('edit', views.UserContactApplicationEditView.as_view(), name='admin-contact-edit')
]   
from common import views
from django.urls import path

urlpatterns = [
    path('settings', views.SettingsView.as_view(), name='settings-admin'),
    path('login', views.LogInView.as_view(), name='login'),
    path('product/<str:pk>/get', views.RetriveProductView.as_view(), name='admin-product-get'),
    path('product/add', views.AddProductView.as_view(), name='admin-product-add'),
    path('product/<str:pk>/update', views.UpdateProductView.as_view(), name='admin-product-update'),
    path('product/<str:pk>/delete', views.DeleteProductView.as_view(), name='admin-product-delete')
]   
from product.landing import views
from django.urls import path

urlpatterns = [
    path('list', views.ProductListView.as_view(), name='product-landing-list')
]   
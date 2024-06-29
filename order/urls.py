from order import views
from django.urls import path

urlpatterns = [
    path('edit/<str:pk>', views.OrderEditStatusVeiw.as_view(), name='admin-order-order')

]   
from product import views
from django.urls import path

urlpatterns = [
    path('list',views.ListProductsView.as_view(), name='admin-product-list'),
    path('detail/<str:pk>', views.RetriveProductView.as_view(), name='admin-product-get'),
    path('add', views.AddProductView.as_view(), name='admin-product-add'),
    path('update/<str:pk>', views.UpdateProductView.as_view(), name='admin-product-update'),
    path('delete/<str:pk>', views.DeleteProductView.as_view(), name='admin-product-delete'),
    path('free/list', views.FreeProductListView.as_view(), name='admin-free-product-list'),
    path('free/add', views.FreeProductAdd.as_view(), name='admin-free-product-add'),
    path('free/detail/<str:pk>', views.FreeProductRetriveView.as_view(), name='admin-free-product-get'),
    path('free/update/<str:pk>', views.FreeProductEdit.as_view(), name='admin-free-product-edit'),
    path('free/delete/<str:pk>', views.DeleteProductView.as_view(), name='admin-free-product-delete')
]   
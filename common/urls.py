from common import views
from django.urls import path

urlpatterns = [
    path('settings', views.SettingsView.as_view(), name='admin-settings'),
    path('page/list', views.PageListView.as_view(), name='admin-page-list'),
    path('page/add', views.AddPageView.as_view(), name='admin-page-add'),
    path('page/get/<str:slug>', views.RetrievePageView.as_view(), name='admin-page-get'),
    path('page/edit', views.EditPageView.as_view(), name='admin-page-edit'),
    path('page/delete/<str:slug>', views.DeletePageView.as_view(), name='admin-page-delete'),
    path('gallery/list',views.ListGalleryView.as_view(), name='admin-gallery-list'),
    path('gallery/add',views.AddGalleryView.as_view(), name='admin-gallery-add'),
    path('gallery/delete/<str:pk>', views.DeleteGalleryView.as_view(), name='admin-gallery-delete'),
]   
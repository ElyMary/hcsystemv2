from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.provider_insert, name='provider-insert'),
    path('', views.provider_show, name='provider-show'),
    path('edit/<int:pk>', views.provider_edit, name='provider-edit'),
    path('remove/<int:pk>', views.provider_remove, name='provider-remove'),
]
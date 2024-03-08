from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.products_insert, name='products-insert'),
    path('', views.products_show, name='products-show'),
    path('edit/<int:pk>', views.products_edit, name='products-edit'),
    path('remove/<int:pk>', views.products_remove, name='products-remove'),
]
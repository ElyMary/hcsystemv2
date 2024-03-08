from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.prvdrcateg_insert, name='provider-categ-insert'),
    path('', views.prvdrcateg_show, name='provider-categ-show'),
    path('edit/<int:pk>', views.prvdrcateg_edit, name='provider-categ-edit'),
    path('remove/<int:pk>', views.prvdrcateg_remove, name='provider-categ-remove'),
]
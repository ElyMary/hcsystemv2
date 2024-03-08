from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.membertype_insert, name='membertype-insert'),
    path('', views.membertype_show, name='membertype-show'),
    path('edit/<int:pk>', views.membertype_edit, name='membertype-edit'),
    path('remove/<int:pk>', views.membertype_remove, name='membertype-remove'),
]
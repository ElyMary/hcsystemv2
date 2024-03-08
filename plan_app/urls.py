from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.plan_insert, name='plan-insert'),
    path('', views.plan_show, name='plan-show'),
    path('edit/<int:pk>', views.plan_edit, name='plan-edit'),
    path('remove/<int:pk>', views.plan_remove, name='plan-remove'),
]
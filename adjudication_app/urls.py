from django.urls import path
from . import views


urlpatterns = [
    path('', views.adju_list, name='adjudi-list'),
    path('dashboard/', views.adju_insert, name='adju-insert'),
]
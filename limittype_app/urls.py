from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.limittype_insert, name='limittype-insert'),
    path('', views.limittype_show, name='limittype-show'),
    path('edit/<int:pk>', views.limittype_edit, name='limittype-edit'),
    path('remove/<int:pk>', views.limittype_remove, name='limittype-remove'),
]
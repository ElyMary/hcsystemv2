from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form, name='login-form'),
    path('dashboard/', views.login_show, name='login-show'),
    # path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    # path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
]
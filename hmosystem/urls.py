"""
URL configuration for hmosystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login_app.urls')),
    path('provider/', include('provider_app.urls')),
    path('prvdrcateg/', include('providercategory_app.urls')),
    path('product/', include('products_app.urls')),
    path('roomtype/', include('roomtype_app.urls')),
    path('limittype/', include('limittype_app.urls')),
    path('membertype/', include('membertype_app.urls')),
    path('plan/', include('plan_app.urls')),
    path('adjudication/', include('adjudication_app.urls')),
]
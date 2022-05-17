"""computer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from app.views import home,compute,compute2,sketch,sketchCompute

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),#添加首页路由
    path('sketch', sketch, name = 'sketch'),#添加首页路由
    path('compute/', compute, name='compute'),
    path('compute2/', compute2, name='compute2'),
    path('sketchCompute/', sketchCompute, name='sketchCompute'),
]

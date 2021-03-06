"""template_lesson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from app01 import views


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'show_time/', views.show_time),
    url(r'query/', views.query),
    url(r'login/', views.login,name='login'),
    url(r'backend/', views.backend),
    url(r'student/', views.student),
    url(r'index01/', views.index01),
    url(r'addbook/', views.addbook),
    url(r'update/', views.update),
    url(r'delete/', views.delete),
    url(r'select/', views.select),

]

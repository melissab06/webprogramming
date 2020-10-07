"""mainApp URL Configuration

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

from django.urls import path, re_path
from phonebook import views
#from django.conf.urls import include, url
#이라고 하면 url(r'^update/([0-9]+)/) 이런식으로 가능

app_name = 'PB'

urlpatterns = [
    re_path(r'^$', views.test),
    path('index/', views.index, name="index"),
    path('add/', views.add, name="add"),
    re_path(r'delete/([0-9]+)/', views.delete, name="delete"),
    re_path(r'^detail/([0-9]+)/', views.detail, name="detail"),
    re_path(r'^update/([0-9]+)/', views.update, name="update"),

]
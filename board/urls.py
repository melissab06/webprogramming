from django.urls import path, re_path, include
from board import views

app_name = 'BD'

urlpatterns = [
    re_path(r'^([0-9]+)/$', views.index, name='index'),
    re_path(r'^add/', views.add, name='add'),
    re_path(r'^detail/([0-9]+)/', views.detail, name="detail"),
    re_path(r'^delete/([0-9]+)/', views.delete, name="delete"), 
    re_path(r'^update/([0-9]+)/', views.update, name="update"), 
    re_path(r'^page/([0-9]+)/$', views.borderPaging, name="page"), 
]
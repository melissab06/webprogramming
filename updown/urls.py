from django.urls import path, include, re_path
from updown import views

app_name = "updown"

urlpatterns = [
    re_path(r'^$', views.index, name="index"), 
    re_path(r'^upload/', views.upload, name="upload"), 
    re_path(r'^download/([0-9a-zA-Zㄱ-힣._]+)/', views.download, name="download"), 
    
]
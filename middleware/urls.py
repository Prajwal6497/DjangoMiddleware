from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('excep/', views.excep, name='excep'),
    path('user/', views.user, name='user'),
]

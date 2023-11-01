
from django.contrib import admin
from django.urls import path, include
from student import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('', views.login, name='login'),
    path('details/', views.details, name='details'),
    path('detail/', views.detail, name='detail'),
    path('join/', views.join, name='join'),

]

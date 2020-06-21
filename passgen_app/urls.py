from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='passgen'),
    path('result/', views.page1, name='generator'),
]

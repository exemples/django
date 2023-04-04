from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='main-index'),
    path('', views.HomeView.as_view(), name='main-home'),
]

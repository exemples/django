from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='rh-index'),
    path('list/', views.emplList, name='rh-empl-list'),
    path('detail/<int:id>/', views.emplDetail, name='rh-empl-detail'),
    path('form/', views.emplForm, name='rh-empl-form'),
]

from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('all-employes-list', views.ListAllEmployes.as_view())
]

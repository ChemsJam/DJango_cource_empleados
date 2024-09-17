from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('employes/all-employes-list', views.ListAllEmployes.as_view()),
    path('employes/all-employes-list-by-department', views.ListAllEmployesByDepartment.as_view()),
]

from django.shortcuts import render
from django.views.generic import (
    ListView
)

from .models import Employe

# Create your views here.

class ListAllEmployes(ListView):
    template_name = 'employes/ListAllEmployes.html'
    model = Employe
    context_object_name = 'employe_list'
    
class ListAllEmployesByDepartment(ListView):
    template_name = 'employes/ListAllByDepartment.html'
    queryset = Employe.objects.filter(
        departmen__name = 'Sistemas'
    )
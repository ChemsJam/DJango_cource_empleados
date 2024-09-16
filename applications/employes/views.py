from django.shortcuts import render
from django.views.generic import (
    ListView
)

from .models import Employe

# Create your views here.

class ListAllEmployes(ListView):
    template_name = 'employes/ListAllEmployes.html'
    model = Employe
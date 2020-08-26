from django.shortcuts import render
from django.views.generic import (
    ListView
)

# Create your views here.
from .models import EmpleadoModel

class ListAllEmployees(ListView):
    template_name = 'persona/list_all.html'
    model = EmpleadoModel
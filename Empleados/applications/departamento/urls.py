from django.contrib import admin
from django.urls import path

def desdeApps(self):
    print("=============== Desde la app departamento===============")

urlpatterns = [
    path('departamento', desdeApps),
]
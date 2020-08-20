from django.contrib import admin
from django.urls import path

def personaApp(self):
    print("=============== Desde la app persona===============")

urlpatterns = [
    path('persona', personaApp),
]
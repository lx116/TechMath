from django.urls import path
from .views import startApp
urlpatterns = [
    path('',startApp,name='Inicio')
]
from django.urls import path
from .views import startApp,AboutUs
urlpatterns = [
    path('',startApp,name='Inicio'),
    path('acercaDe/',AboutUs,name='Acerca de'),
]
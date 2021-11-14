from django.urls import path
from .views import startApp,AboutUs,PresentatioScreen,funcioCentral
urlpatterns = [
path('',PresentatioScreen,name='Home'),
    path('inicio/',startApp,name='Inicio'),
    path('acercaDe/',AboutUs,name='Acerca de'),
    path('funcionCentral/',funcioCentral,name='centro')

]
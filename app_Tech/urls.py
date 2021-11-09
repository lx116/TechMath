from django.urls import path
from .views import startApp,AboutUs,PresentatioScreen
urlpatterns = [
    path('inicio/',startApp,name='Inicio'),
    path('acercaDe/',AboutUs,name='Acerca de'),
    path('',PresentatioScreen,name='Home')
]
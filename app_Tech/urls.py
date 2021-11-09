from django.urls import path
from .views import startApp,AboutUs,PresentatioScreen,Documentation,interpolacionLineal
urlpatterns = [
    path('inicio/',startApp,name='Inicio'),
    path('acercaDe/',AboutUs,name='Acerca de'),
    path('',PresentatioScreen,name='Home'),
    path('documentacion/',Documentation,name='Documentacion'),
    path('formulaOne/',interpolacionLineal,name='linela1')
]
from django.urls import path
from .views import startApp,AboutUs,PresentatioScreen,interpolLineal,interpolacionLagrange,interpolacionNewton,interpolacionCuadratica
urlpatterns = [
    path('inicio/',startApp,name='Inicio'),
    path('acercaDe/',AboutUs,name='Acerca de'),
    path('',PresentatioScreen,name='Home'),
    path('interpolacionLineal/',interpolLineal,name='linela1'),
    path('interpolacionLagrange/',interpolacionLagrange,name='Lagrange'),
    path('interpolacionNewton/',interpolacionNewton,name='Newton'),
    path('interpolacionCuadratica/',interpolacionCuadratica,name='Cuadratica')
]
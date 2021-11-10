import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def startApp(request):

    return render(request,'appOne.html')

def AboutUs(request):

    return render(request,'AboutUs.html')

def PresentatioScreen(request):

    return render(request, 'index.html')

def Documentation(request):

    return  render(request,'documentation.html')


def interpolLineal(request):

    X = np.linspace(-np.pi, np.pi, 5)
    Xexp = np.linspace(-np.pi, np.pi, 21)
    Yexp = np.sin(Xexp)

    Y = np.interp(X, Xexp, Yexp)
    print(Y)
    plt.plot(Xexp, Yexp)
    plt.plot(X, Y, 10)
    plt.show()

def interpolacionCuadratica(request):
    pass

def interpolacionLagrange(request):

    #Datos
    xi = np.array([0, 0.2, 0.3, 0.4])
    fi = np.array([1, 1.6, 1.7, 2.0])

    #Procedimiento

    n = len(xi)
    x = sym.symbols("x")
    polinomio = 0
    for i in range(0, n, 1):
        numerador = 1
        denominador = 1

    for j in range(0, n, 1):
        if i != j:
            numerador = numerador * (x - xi[j])
            denominador = denominador * (xi[i] - xi[j])
            termino = (numerador / denominador) * fi[i]
            polinomio = polinomio + termino
            polisimple = sym.expand(polinomio)
            px = sym.lambdify(x, polinomio)

    #Vectores_para_graficar

    muestra = 51
    a = np.min(xi)
    b = np.max(xi)
    p_xi = np.linspace(a, b, muestra)
    pfi = px(p_xi)

    #salida
    print('Polinomio')
    print(polinomio)
    print('Polisimple:')
    print(polisimple)

    #Grafica
    plt.plot(xi, fi, 'o')
    plt.plot(p_xi, pfi)
    plt.show()


def interpolacionNewton(request):
    pass



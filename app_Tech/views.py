import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy import interpolate
from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def startApp(request):
    return render(request, 'appOne.html')


def AboutUs(request):
    return render(request, 'AboutUs.html')


def PresentatioScreen(request):
    return render(request, 'index.html')


@csrf_exempt
def funcioCentral(request):
    req = request.POST['data']
    data = json.loads(req)

    variablesX = data.get('X')
    variablesY = data.get('Y')
    valorZ= float(data.get('Z'))
    print(variablesX)
    print(variablesY)

    arrayX = []
    arrayY = []

    for var in variablesX:
        arrayX.append(float(var))


def interpolLineal(request):

   #Aqui van los datos de los inputs
    x = np.array([3, 5, 7])
    y = np.array([10, 14, 22])

   #Se interpola y "xi" es la x a buscar

    polinomio = interpolate.interp1d(x, y)

    xi = 4
    yi = polinomio(xi)


    print(yi)


   #Se muestra la tabla
    plt.plot(x, y, 'o:', xi, yi, 'sr')
    plt.grid()
    plt.title('Grafica', fontsize=16)
    plt.text(xi, yi, ' interpolacion ' + str(yi))
    plt.show()

def interpolacionCuadratica(request):
    # Aqui van los datos de los inputs
    x = np.array([3, 5, 7])
    y = np.array([10, 14, 22])

    cuadratico = interpolate.interp1d(x, y, kind='quadratic')
    xi = 4
    ki = cuadratico(xi)
    print(ki)

def interpolacionLagrange(request):
    #Datos de la tabla
    x = np.array([1, 4, 6, 8])
    y = np.array([0, 1.386294, 1.791760, 2.079441])

    #Calculo
    poly = interpolate.lagrange(x, y)

    #Imprime - FALTA LA TABLA
    print(poly)


def interpolacionNewton(request):
 pass
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
    valorZ = float(data.get('Z'))
    print(variablesX)
    print(variablesY)

    arrayX = []
    arrayY = []

    for var in variablesX:
        arrayX.append(float(var))

    for var in variablesY:
        arrayY.append(float(var))

    print(arrayX)
    print(arrayY)
    print(valorZ)

    #interpolLineal(arrayX, arrayY, valorZ)
    #interpolacionCuadratica(arrayX,arrayY,valorZ)
    interpolacionLagrange(arrayX,arrayY,valorZ)

def interpolLineal(arrayX, arrayY, valorZ):
    # Aqui van los datos de los inputs
    x = np.array(arrayX)
    y = np.array(arrayY)

    # Se interpola y "xi" es la x a buscar

    polinomio = interpolate.interp1d(x, y)

    xi = valorZ
    yi = polinomio(xi)

    print(yi)

    # Se muestra la tabla
    plt.plot(x, y, 'o:', xi, yi, 'sr')
    plt.grid()
    plt.title('Grafica', fontsize=16)
    plt.text(xi, yi, ' interpolacion ' + str(yi))
    plt.show()

    return yi


def interpolacionCuadratica(arrayX,arrayY,valorZ):
    # Aqui van los datos de los inputs
    x = np.array(arrayX)
    y = np.array(arrayY)

    cuadratico = interpolate.interp1d(x, y, kind='quadratic')
    xi = valorZ
    ki = cuadratico(xi)
    print(ki)

    return ki

def interpolacionLagrange(arrayX,arrayY,valorZ):
    # Datos de la tabla
    x = np.array(arrayX)
    y = np.array(arrayY)

    # Calculo
    poly = interpolate.lagrange(x, y)

    # Imprime - FALTA LA TABLA
    print(poly)


def interpolacionNewton(request):
    # INGRESO , Datos de prueba
    xi = np.array([3.2, 3.8, 4.2, 4.5])
    fi = np.array([5.12, 6.42, 7.25, 6.85])

    # PROCEDIMIENTO

    # Tabla de Diferencias Divididas Avanzadas
    titulo = ['i   ', 'xi  ', 'fi  ']
    n = len(xi)
    ki = np.arange(0, n, 1)
    tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
    tabla = np.transpose(tabla)

    # diferencias divididas vacia
    dfinita = np.zeros(shape=(n, n), dtype=float)
    tabla = np.concatenate((tabla, dfinita), axis=1)

    # Calcula tabla, inicia en columna 3
    [n, m] = np.shape(tabla)
    diagonal = n - 1
    j = 3
    while (j < m):
        # Añade título para cada columna
        titulo.append('F[' + str(j - 2) + ']')

        # cada fila de columna
        i = 0
        paso = j - 2  # inicia en 1
        while (i < diagonal):
            denominador = (xi[i + paso] - xi[i])
            numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
            tabla[i, j] = numerador / denominador
            i = i + 1
        diagonal = diagonal - 1
        j = j + 1

    # POLINOMIO con diferencias Divididas
    # caso: puntos equidistantes en eje x
    dDividida = tabla[0, 3:]
    n = len(dfinita)

    # expresión del polinomio con Sympy
    x = sym.Symbol('x')
    polinomio = fi[0]
    for j in range(1, n, 1):
        factor = dDividida[j - 1]
        termino = 1
        for k in range(0, j, 1):
            termino = termino * (x - xi[k])
        polinomio = polinomio + termino * factor

    # simplifica multiplicando entre (x-xi)
    polisimple = polinomio.expand()

    # polinomio para evaluacion numérica
    px = sym.lambdify(x, polisimple)

    # Puntos para la gráfica
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a, b, muestras)
    pfi = px(pxi)

    # SALIDA
    np.set_printoptions(precision=4)
    print('Tabla Diferencia Dividida')
    print([titulo])
    print(tabla)
    print('dDividida: ')
    print(dDividida)
    print('polinomio: ')
    print(polinomio)
    print('polinomio simplificado: ')
    print(polisimple)

    # Gráfica
    plt.plot(xi, fi, 'o', label='Puntos')
    ##for i in range(0,n,1):
    ##plt.axvline(xi[i],ls='--', color='yellow')
    plt.plot(pxi, pfi, label='Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Diferencias Divididas - Newton')
    plt.show()
    pass

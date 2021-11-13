from urllib.parse import urljoin

import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import os,uuid
from scipy import interpolate
from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def startApp(request):
    return render(request, 'appOne.html')


def AboutUs(request):
    return render(request, 'AboutUs.html')


def PresentatioScreen(request):
    return render(request, 'index.html')

@csrf_exempt
def funcioCentral(request):
    path_resultados = os.path.join(settings.MEDIA_ROOT,'resultados')
    if not os.path.exists(path_resultados):
        os.makedirs(path_resultados)

    req = request.POST['data']
    data = json.loads(req)

    name = uuid.uuid4()

    print(name)

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

    # Interpolacion lineal
    xlineal = np.array(arrayX)
    ylineal = np.array(arrayY)
    success= False
    imagen = None
    mensaje = ''

    try:
        polinomio = interpolate.interp1d(xlineal, ylineal)

        xiL = valorZ
        linealR = polinomio(xiL)
        print(linealR)

        # Interpolacion Cuadratica
        xcuad = np.array(arrayX)
        ycuad = np.array(arrayY)

        cuadratico = interpolate.interp1d(xcuad, ycuad, kind='quadratic')
        xiC = valorZ
        cuadR = cuadratico(xiC)

        print(cuadR)

        # Lagrange
        xlag = np.array(arrayX)
        ylag = np.array(arrayY)

        lagR = interpolate.lagrange(xlag, ylag)

        print(lagR)

        fig, ax = plt.subplots()

        plt.plot(arrayX, arrayY, xiL, linealR, 'o:', color='tab:purple', label='Lineal')
        plt.text(xiL, linealR, str(linealR))
        plt.plot(arrayX, arrayY, xiC, cuadR, 'o:', color='tab:green', label='Cuadratica')
        plt.text(xiC, cuadR, str(cuadR))

        u = plt.plot(np.array(arrayX), np.array(arrayY), 'ro')
        t = np.linspace(0, 1, len(np.array(arrayX)))
        pxLagrange = interpolate.lagrange(t, np.array(arrayX))
        pyLagrange = interpolate.lagrange(t, np.array(arrayY), )
        n = 100
        ts = np.linspace(t[0], t[-1], n)
        xLagrange = pxLagrange(ts)
        yLagrange = pyLagrange(ts)
        plt.plot(xLagrange, yLagrange, 'b-', color='tab:red', label='Lagrange')
        plt.legend(loc='upper right')
        success = True

        file_name='resultados/{}.png'.format(name)
        path = os.path.join(settings.MEDIA_ROOT,file_name)
        #path = "recursos/static/web/img/{}.png".format(name)

        print(path)

        my_path = os.path.abspath(__file__)
        print(my_path)
        plt.savefig(path)
        plt.show()
        imagen=urljoin(settings.MEDIA_URL,file_name)

    except ValueError as e:
        mensaje='Ha ocurrido un erro {}'.format(str(e))

    return JsonResponse({'imagen':imagen,'success':success,'mensaje':mensaje})



def interpolLineal(arrayX, arrayY, valorZ):
    xlineal = np.array(arrayX)
    ylineal = np.array(arrayY)

    polinomio = interpolate.interp1d(xlineal, ylineal)

    xiL = valorZ
    linealR = polinomio(xiL)

    print(linealR)

    linealArray = [xiL, linealR]

    return linealArray


def interpolacionCuadratica(arrayX, arrayY, valorZ):
    # Aqui van los datos de los inputs
    x = np.array(arrayX)
    y = np.array(arrayY)

    cuadratico = interpolate.interp1d(x, y, kind='quadratic')
    xi = valorZ
    ki = cuadratico(xi)

    plt.plot(x, y, 'o:', xi, ki)

    plt.title('Grafica', fontsize=16)
    plt.text(xi, ki, ' interpolacion cuadratica ' + str(ki))

    print(ki)
    print(cuadratico)

    arrayResultado = [xi, cuadratico, ki]

    return arrayResultado


def interpolacionLagrange(arrayX, arrayY, valorZ):
    # Datos de la tabla
    x = np.array(arrayX)
    y = np.array(arrayY)

    # Calculo
    poly = interpolate.lagrange(x, y)

    # Imprime
    plt.figure()
    u = plt.plot(x, y, 'ro')
    t = np.linspace(0, 1, len(x))
    pxLagrange = interpolate.lagrange(t, x)
    pyLagrange = interpolate.lagrange(t, y)
    n = 100
    ts = np.linspace(t[0], t[-1], n)
    xLagrange = pxLagrange(ts)
    yLagrange = pyLagrange(ts)
    plt.plot(xLagrange, yLagrange, 'b-', label="Polynomial")

    print(poly)
    arrayResultados = [xLagrange, yLagrange]

    return arrayResultados


def interpolacionNewton(x, y, n, xi, yint, ea):
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

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

    lagR =0
    linealR=0
    cuadR =0

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

        plt.plot(arrayX, arrayY, xiL, linealR, 'o:', color='tab:blue', label='Lineal')
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
        mensaje='Ha ocurrido un error {}'.format(str(e))

    send_lagR = str(lagR)
    send_linealR = str(linealR)
    send_CuadR = str(cuadR)

    return JsonResponse({'imagen':imagen,'success':success,'mensaje':mensaje,'lagrange_resultado':send_lagR, 'lineal_resultado':send_linealR,'cuadratica':send_CuadR})

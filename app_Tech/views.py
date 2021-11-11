import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
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

    for var in variablesY:
        arrayY.append(float(var))

    print(arrayX)
    print(arrayY)
    print(valorZ)

def interpolLineal(request):
    req = request.POST['data']
    data = json.loads(req)

    print(data)

    a = int(data.get('a'))
    b = int(data.get('b'))
    c = int(data.get('c'))

    X = np.linspace(-np.pi, np.pi, a)
    Xexp = np.linspace(-np.pi, np.pi, b)
    Yexp = np.sin(Xexp)

    Y = np.interp(X, Xexp, Yexp)
    print(Y)
    plt.plot(Xexp, Yexp)
    plt.plot(X, Y, c)

    print(X)
    print(Xexp)
    print(Yexp)
    plt.savefig('recursos/static/web/img/fig.png')
    plt.show()

    list_productos = []

    for list_valores in Y:
        list_productos.append(
            {
                'ValOne': list_valores
            }
        )
    print(list_productos)

    return JsonResponse({'resultado': list_productos})


def interpolacionCuadratica(request):
    # INGRESO
    xi = [0, 0.2, 0.3, 0.4]
    fi = [1, 1.6, 1.7, 2.0]
    # muestras = tramos+1
    muestras = 101

    # PROCEDIMIENTO
    # Convierte a arreglos numpy
    xi = np.array(xi)
    B = np.array(fi)
    n = len(xi)

    # Matriz Vandermonde D
    D = np.zeros(shape=(n, n), dtype=float)
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            potencia = (n - 1) - j  # Derecha a izquierda
            D[i, j] = xi[i] ** potencia

    # Aplicar métodos Unidad03. Tarea
    # Resuelve sistema de ecuaciones A.X=B
    coeficiente = np.linalg.solve(D, B)

    # Polinomio en forma simbólica
    x = sym.Symbol('x')
    polinomio = 0
    for i in range(0, n, 1):
        potencia = (n - 1) - i  # Derecha a izquierda
        termino = coeficiente[i] * (x ** potencia)
        polinomio = polinomio + termino

    # Polinomio a forma Lambda
    # para evaluación con vectores de datos xin
    px = sym.lambdify(x, polinomio)

    # Para graficar el polinomio en [a,b]
    a = np.min(xi)
    b = np.max(xi)
    xin = np.linspace(a, b, muestras)
    yin = px(xin)

    # Usando evaluación simbólica
    ##yin = np.zeros(muestras,dtype=float)
    ##for j in range(0,muestras,1):
    ##    yin[j] = polinomio.subs(x,xin[j])

    # SALIDA
    print('Matriz Vandermonde: ')
    print(D)
    print('los coeficientes del polinomio: ')
    print(coeficiente)
    print('Polinomio de interpolación: ')
    print(polinomio)
    print('\n formato pprint')
    sym.pprint(polinomio)

    # Grafica
    plt.plot(xi, fi, 'o', label='[xi,fi]')
    plt.plot(xin, yin, label='p(x)')
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.legend()
    plt.title(polinomio)
    plt.show()


def interpolacionLagrange(request):
    # Datos
    xi = np.array([0, 0.2, 0.3, 0.4])
    fi = np.array([1, 1.6, 1.7, 2.0])

    # Procedimiento

    n = len(xi)
    x = sym.symbols("x")

    numerador = 0
    denominador = 0
    polisimple = 0
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

    # Vectores_para_graficar

    muestra = 51
    a = np.min(xi)
    b = np.max(xi)
    p_xi = np.linspace(a, b, muestra)
    pfi = px(p_xi)

    # salida
    print('Polinomio')
    print(polinomio)
    print('Polisimple:')
    print(polisimple)

    # Grafica
    plt.plot(xi, fi, 'o')
    plt.plot(p_xi, pfi)
    plt.show()

    return JsonResponse({'resultado': muestra})


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

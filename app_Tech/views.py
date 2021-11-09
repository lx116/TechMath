from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
import numpy as np
import matplotlib.pyplot as ptl
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def startApp(request):

    return render(request,'appOne.html')

def AboutUs(request):

    return render(request,'AboutUs.html')

def PresentatioScreen(request):

    return render(request,'index.html')

def Documentation(request):

    return  render(request,'documentation.html')


def interpolLineal(request):

    X = np.linspace(-np.pi, np.pi, 5)
    Xexp = np.linspace(-np.pi, np.pi, 21)
    Yexp = np.sin(Xexp)

    Y = np.interp(X, Xexp, Yexp)

    ptl.plot(Xexp, Yexp)
    ptl.plot(X, Y, 10)
    ptl.show()

def interpolacionCuadratica(request):
    pass

def interpolacionLagrange(request):
    pass

def interpolacionNewton(request):
    pass



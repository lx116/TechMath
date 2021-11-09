from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from recursos.static.pythonCodes import interpolacionLineal

def startApp(request):

    return render(request,'appOne.html')

def AboutUs(request):

    return render(request,'AboutUs.html')

def PresentatioScreen(request):

    return render(request,'index.html')

def Documentation(request):

    return  render(request,'documentation.html')


def interpolLineal(request):


    interpolacionLineal.interpolLineal()


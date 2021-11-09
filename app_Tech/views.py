from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def startApp(request):

    return render(request,'index.html')

def AboutUs(request):

    return render(request,'AboutUs.html')
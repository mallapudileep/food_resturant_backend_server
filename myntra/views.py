from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def clg(req):
    return render(req,'clg.html')


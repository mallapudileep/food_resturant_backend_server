from django.shortcuts import render

# Create your views here.
def model(req):
    return render(req,'base.html')
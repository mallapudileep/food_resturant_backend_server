from django.shortcuts import render

# Create your views here.

def amazon_page(req):
    return render(req,'amazo.html',{'name':'dileep'})
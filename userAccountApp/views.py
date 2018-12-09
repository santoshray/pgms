from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    res_dict = {}
    return render(request,'useraccount/index.html',context=res_dict)

def register(request):
    res_dict = {}
    return render(request,'useraccount/index.html',context=res_dict)

def edit(request):
    res_dict={}
    return render(request,'useraccount/index.html',context=res_dict)

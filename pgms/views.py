from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    res_dict = {}
    return render(request,'index.html',context=res_dict)

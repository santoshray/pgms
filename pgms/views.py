from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    res_dict = {}
    return render(request,'index.html',context=res_dict)


def contact(request):
    res_dict = {}
    if request.method=="GET":
        return render(request,'contact.html',context=res_dict)

    if request.method=="POST":
        post_content = request.POST
        print(post_content)
        return render(request,'contact.html',context=res_dict)

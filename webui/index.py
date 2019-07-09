from django.http import HttpResponse
from django.shortcuts import render
import time
 
def hello(request):
    context = {}
    context["name"] = "YZP"
    return render(request,"index.html",context)

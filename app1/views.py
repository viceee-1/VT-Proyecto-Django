from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def v1_app1(request):
    return HttpResponse("<h1 style='color: purple;'>Vista 1 App2</h1>")

def v2_app1(request):
    return HttpResponse("<h1 style='color: purple;''>Vista 2 App2</h1>")

from django.http import HttpResponse
from django.shortcuts import render
def saludo(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Hasta luego")

def adulto(request,edad):
    if(edad>=18):
        return HttpResponse("Mayor de edad")
    else:
        return HttpResponse("Menor de edad")

def simple(request):
    return render(request,'simple.html',{})

def dinamico(request,name):
    categories = ['code','design','marketing','python']
    context = {'name':name,'categories':categories}
    return render(request,'dinamico.html',context)
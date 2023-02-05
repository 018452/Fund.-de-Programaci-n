from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio_ver (*variable,**variableid):
    return HttpResponse ("<h1>Pagina de inicio</h1>")

#logica de negocios#
'''
def sumadelos10primerosnumeros (request,*variable,**variableid):
    n=10 
    acum=0
    for i in range (n+1):
        acum=acum+i
    return render (request,"home.html",{'acum':acum}) 
'''
def sumadelos10primerosnumeros (request,*variable,**variableid):
    n=100 
    acum=0
    for i in range (n+1):
        acum=acum+i
    return render (request,'home.html',{'resultado':acum}) 
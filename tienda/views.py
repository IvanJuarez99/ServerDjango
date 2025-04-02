from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def productos(request):
    #return HttpResponse("Hola, este es el listado de productos test2")
    return render(request, "tienda/productos.html")

def arreglos(request):
    #return HttpResponse("Hola, este es el listado de arreglos test2")
    return render(request, "tienda/arreglos.html")
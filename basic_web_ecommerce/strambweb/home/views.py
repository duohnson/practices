from django.shortcuts import render

def index(request):
    from tienda.models import Producto
    ofertas = Producto.objects.prefetch_related('imagenes').filter(is_oferta=True)
    return render(request, 'home/index.html', {'ofertas': ofertas})

def contacto(request):
    return render(request, 'home/contacto.html')

def tienda(request):
    return render(request, 'home/tienda.html')
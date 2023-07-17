from django.shortcuts import render, redirect
from .models import Laboratorio

def index(request):
    laboratorios = Laboratorio.objects.all()
    context = {
        'laboratorios': laboratorios
    }
    return render(request, 'index.html', context)

def mostrar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count
    return render(request, 'mostrar_laboratorios.html', {'laboratorios': laboratorios, 'visit_count': visit_count})


def insertar_laboratorio(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        Laboratorio.objects.create(nombre=nombre, ciudad=ciudad, pais=pais)
        return redirect('mostrar_laboratorios')
    return render(request, 'insertar_laboratorio.html')

def editar_laboratorio(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
    if request.method == 'POST':
        laboratorio.nombre = request.POST['nombre']
        laboratorio.ciudad = request.POST['ciudad']
        laboratorio.pais = request.POST['pais']
        laboratorio.save()
        return redirect('mostrar_laboratorios')
    return render(request, 'editar_laboratorio.html', {'laboratorio': laboratorio})

def eliminar_laboratorio(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar_laboratorios')
    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})


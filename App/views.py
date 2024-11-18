from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    return render(request,"index.html")

def base(request):
    return render(request,"base.html")

def reservacion(request):
    return render(request,"reservacion.html")

def postreservacion(request):
    nom = request.POST.get('nombre')
    corr = request.POST.get('correo')
    tel = request.POST.get('telefono')
    fech = request.POST.get('fecha')
    hor = request.POST.get('hora')
    amp = request.POST.get('ampm')
    servici = request.POST.get('servicio')

    models.reservacion.objects.create(
        nombre = nom,
        correo = corr,
        telefono = tel,
        fecita = fech,
        hora = hor,
        ampm = amp,
        servicio = servici
    )

    return redirect('inicio')

def promociones(request):
    return render(request,"promociones.html")

def recordatorios(request):
    return render(request,"recordatorios.html")

def inicio(request):
    return render(request,"inicio.html")

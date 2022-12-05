from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import loader
import datetime
# Create your views here.


def crearfamiliar(request):
    
    familiar = Familia(nombre="carina", edad=58, fecha=datetime.datetime.now())
    familiar.save()
    fecha=datetime.datetime.today()
    nuevofamiliar=f"Nuevo familiar: {familiar.nombre}, con una edad de :{familiar.edad}, Hoy es {fecha}"
    
    return HttpResponse (nuevofamiliar)

def familiareshtml(request):
    familiar = Familia(nombre="Lucas", edad=48, fecha=datetime.datetime.now())
    familiar2 = Familia(nombre="Alberto", edad=28, fecha=datetime.datetime.now())
    familiar3 = Familia(nombre="carina", edad=58, fecha=datetime.datetime.now())

    familiares={"nombre":"Lucas", "edad":48, "fecha":datetime.datetime.now(),

    "nombre2":"Alberto", "edad2":28, "fecha2":datetime.datetime.now(),

    "nombre3":"carina", "edad3":48, "fecha3":datetime.datetime.now()}
    
    template = loader.get_template("familiatemplate.html")
    nuevosfamiliares = template.render(familiares)
    return HttpResponse(nuevosfamiliares)


def crearfamiliar2(request):
    familiar = Familia(nombre="Lucas", edad=48, fecha=datetime.datetime.now())
    familiar2 = Familia(nombre="Alberto", edad=28, fecha=datetime.datetime.now())
    familiar3 = Familia(nombre="carina", edad=58, fecha=datetime.datetime.now())
    familiar.save()
    familiar2.save()
    familiar3.save()
    
    familiares={"nombre":familiar.nombre, "edad":familiar.edad, "fecha":familiar.fecha,
    "nombre2":familiar2.nombre, "edad2":familiar2.edad, "fecha2":familiar2.fecha,
    "nombre3":familiar3.nombre, "edad3":familiar3.edad, "fecha3":familiar3.fecha,}

    template=loader.get_template("familiatemplate.html")
    nuevosfamiliares = template.render(familiares)
    return HttpResponse(nuevosfamiliares)
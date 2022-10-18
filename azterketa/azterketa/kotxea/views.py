from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from kotxea.models import Kotxea, Pertsona

# Create your views here.


def index(request):
    return render(request, 'index.html')


def kotxelista(request):
    kotxeak = Kotxea.objects.all
    pertsonak = Pertsona.objects.all
    return render(request, 'kotxea.html', {'kotxea': kotxeak, 'pertsona':pertsonak})


def add(request):
    return render(request, 'add.html')


def addrecord(request):
    izena = request.POST['izena']
    marka = request.POST['marka']
    data = request.POST['data']

    kotxea= Kotxea(izena=izena, marka=marka, data=data)
    kotxea.save()
    return HttpResponseRedirect(reverse('kotxea'))

def update(request, id):
    kotxea = Kotxea.objects.get(id=id)
    return render(request, 'update.html', {'kotxea': kotxea})

def updaterecord(request, id):
    izena = request.POST['izena']
    marka = request.POST['marka']
    data = request.POST['data']
    kotxea = Kotxea.objects.get(id=id)
    kotxea.izena = izena
    kotxea.marka = marka
    kotxea.data = data
    kotxea.save()
    return HttpResponseRedirect(reverse('kotxea'))

def delete(request, id):
    kotxea = Kotxea.objects.get(id=id)
    kotxea.delete()
    return HttpResponseRedirect(reverse('kotxea'))

def addPer(request):
    return render(request, 'addPer.html')


def addrecordPer(request):
    id_kotxea = request.POST['id_kotxea']
    kotxea = Kotxea.objects.get(id=id_kotxea)
    izena = request.POST['izena']
    abizena = request.POST['abizena']

    pertsona= Pertsona(izena=izena, abizena=abizena, id_kotxea=kotxea)
    pertsona.save()
    return HttpResponseRedirect(reverse('kotxea'))

def deletePer(request, id):
    pertsona = Pertsona.objects.get(id=id)
    pertsona.delete()
    return HttpResponseRedirect(reverse('kotxea'))
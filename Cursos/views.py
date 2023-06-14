from django.shortcuts import render
from .models import Categoria,Cursos


def infor(request):
    inform = Cursos.objects.all()
    context = {'informa' : inform}
    return render(request,'Cursos/informatica.html',context)

def ali(request):
    context={'alimentos': ali}
    return render(request,'Cursos/alimentos.html',context)

def api(request):
    context={'apicultura': api}
    return render(request,'Cursos/apicultura.html',context)

def index(request):
    return render(request, 'Cursos/index.html')


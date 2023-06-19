from django.shortcuts import render
from .models import Categoria,Cursos
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'Cursos/index.html')

def detal_curso(request,id_curso):
    curso = get_object_or_404(Cursos, id=id_curso)
    context={'obj' : curso}
    
    return render(request,'Cursos/cursos.html', context)

def lis_curso(request):
    cursos = Cursos.objects.all()
    context = {'listar_cursos' : cursos} 
    
    return render(request,'Cursos/lista_cursos.html',context)




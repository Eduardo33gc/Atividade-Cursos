from django.shortcuts import render
from .models import Curso
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    postagens = Curso.objects.all()
    context = {'lista_postagens' : postagens} 
    context = {'mensagem': 'Conheça o IFRN - Campus Pau dos Ferros'}
    return render(request, 'core/index.html', context)

def sobre_mim(request):
    context = {'mensagem': 'Conheça mais sobre o desenvolvedor'}
    return render(request, 'core/sobre.html', context)

def detalhes(request, id_curso):
    curso = get_object_or_404(Curso, id = id_curso)
    context = {'objeto' : curso}
    return render(request,'core/detalhecurso.html',context)

def lista_postagens(request):
    postagens = Curso.objects.all()
    context = {'lista_postagens' : postagens} 
    return render(request,'core/cursos.html',context)

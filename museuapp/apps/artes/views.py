from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArteForm
from .models import Arte
from historias.models import Historia
from valores.models import Valor
from categories.models import Category
from artistas.models import Artista

# Create your views here.
def add_arte(request):
    template_name = 'artes/add_arte.html'
    context = {}
    if request.method == 'POST':
        form = ArteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('artes:list_artes')
    form = ArteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_artes(request):
    template_name = 'artes/list_artes.html'
    artes = Arte.objects.filter()
    context = {
        'artes': artes
    }
    return render(request, template_name, context)

def edit_arte(request, id_arte):
    template_name = 'artes/add_arte.html'
    context ={}
    arte = get_object_or_404(Arte, id=id_arte)
    if request.method == 'POST':
        form = ArteForm(request.POST, instance=arte)
        if form.is_valid():
            form.save()
            return redirect('artes:list_artes')
    form = ArteForm(instance=arte)
    context['form'] = form
    return render(request, template_name, context)

def view_arte(request, id_arte):
    template_name = 'artes/view_arte.html'
    context ={}
    arte = get_object_or_404(Arte, id=id_arte)
    if request.method == 'POST':
        form = ArteForm(request.POST, instance=arte)
        if form.is_valid():
            form.save()
            return redirect('artes:list_artes')
    form = ArteForm(instance=arte)
    context['form'] = form
    return render(request, template_name, context)

def delete_arte(request, id_arte):
    arte = Arte.objects.get(id=id_arte)
    arte.delete()
    return redirect('artes:list_artes')

def view_arte(request, id_arte):
    template_name = 'artes/view_arte.html'
    context = {}

    arte = get_object_or_404(Arte, id=id_arte)
    context['artes'] = arte

     #Buscar pelo artista relacionada a essa arte,se existir
    artista = Artista.objects.filter(id=arte.idartista).first()
    context['artistas'] = artista

    # Busca pela história relacionada a esta arte, se existir
    historia = Historia.objects.filter(id=arte.idhistoria).first()
    context['historias'] = historia

    # Busca pelo valor relacionado a esta arte, se existir
    valor = Valor.objects.filter(id=arte.idvalor).first()
    context['valores'] = valor

    # Busca pela categoria relacionada a esta arte, se existir
    category = Category.objects.filter(id=arte.idcategoria).first()
    context['categories'] = category

    return render(request, template_name, context)
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArteForm
from .models import Arte

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

def delete_arte(request, id_arte):
    arte = Arte.objects.get(id=id_arte)
    arte.delete()
    return redirect('artes:list_artes')


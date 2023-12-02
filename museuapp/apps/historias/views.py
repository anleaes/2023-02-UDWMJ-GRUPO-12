
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HistoriaForm
from .models import Historia

# Create your views here.

def add_historia(request):
    template_name = 'historias/add_historia.html'
    context = {}
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('historias:list_historias')
    form = HistoriaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_historias(request):
    template_name = 'historias/list_historias.html'
    historias = Historia.objects.filter()
    context = {
        'historias': historias
    }
    return render(request, template_name, context)

def edit_historia(request, id_historia):
    template_name = 'historias/add_historia.html'
    context ={}
    historia= get_object_or_404(Historia, id=id_historia)
    if request.method == 'POST':
        form = HistoriaForm(request.POST, instance=historia)
        if form.is_valid():
            form.save()
            return redirect('historias:list_historias')
    form = HistoriaForm(instance=historia)
    context['form'] = form
    return render(request, template_name, context)

def delete_historia(request, id_historia):
    historia = Historia.objects.get(id=id_historia)
    historia.delete()
    return redirect('historias:list_historias')

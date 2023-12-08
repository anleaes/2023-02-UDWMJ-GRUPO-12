from django.shortcuts import render, get_object_or_404, redirect
from .forms import ValorForm
from .models import Valor


# Create your views here.


def add_valor(request):
    template_name = 'valores/add_valor.html'
    context = {}
    if request.method == 'POST':
        form = ValorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('valores:list_valores')
    form = ValorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_valores(request):
    template_name = 'valores/list_valores.html'
    valores = Valor.objects.filter()
    context = {
        'valores': valores
    }
    return render(request, template_name, context)


def edit_valor(request, id_valor):
    template_name = 'valores/add_valor.html'
    context ={}
    valor= get_object_or_404(Valor, id=id_valor)
    if request.method == 'POST':
        form = ValorForm(request.POST, instance=valor)
        if form.is_valid():
            form.save()
            return redirect('valores:list_valores')
    form = ValorForm(instance=valor)
    context['form'] = form
    return render(request, template_name, context)


def delete_valor(request, id_valor):
    valor = Valor.objects.get(id=id_valor)
    valor.delete()
    return redirect('valores:list_valores')

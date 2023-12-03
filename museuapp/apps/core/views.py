from django.shortcuts import render
from artes.models import Arte

# Create your views here.
def home(request):
    template_name ='core/home.html'
    artes = Arte.objects.filter()
    context = {
        'artes': artes
    }
    return render(request, template_name, context)


from django import forms
from .models import Valor

class ValorForm(forms.ModelForm):

    class Meta:
        model = Valor
        exclude = ('created_on' , 'updated_on',)

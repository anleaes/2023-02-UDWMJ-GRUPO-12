from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):

    class Meta:
        model = Historia
        exclude = ('created_on' , 'updated_on',)

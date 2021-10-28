from django.db import models
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date'}),
    )
    class Meta:
        model = Cliente
        fields = ['nome', 'data_nascimento', 'endereco', 'telefone']

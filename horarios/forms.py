from django.db import models
from django import forms
from django.forms import widgets
from .models import Agenda
from clientes.models import Cliente
from datetime import date


class AgendaForm(forms.ModelForm):
    dia = forms.DateField(
        label='Dia',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'value': date.today()}),
    )
    horario = forms.TimeField(
        label='Horário',
        widget=forms.DateInput(
            format='%H:%M', attrs={'type': 'time'}),
    )
    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Cliente.objects.all().order_by('nome'),
        required=True,        
    )
    class Meta:
        model = Agenda
        fields = ['dia', 'horario', 'cliente', 'status_atendimento']

from django.db import models
from django import forms
from .models import Agenda
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
    class Meta:
        model = Agenda
        fields = ['dia', 'horario', 'cliente']

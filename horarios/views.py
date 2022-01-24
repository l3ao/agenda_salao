from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from horarios.models import Agenda
from .forms import AgendaForm


class CreateAgenda(SuccessMessageMixin, CreateView):
    template_name = 'horarios/agenda_form.html'
    form_class = AgendaForm
    success_url = reverse_lazy('list-agenda')
    success_message = "Horário foi criado com sucesso!"


class ListAgenda(ListView):
    model = Agenda

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        dia = request.GET.get('data_busca', None)
        dia = datetime.strptime(dia, '%Y-%m-%d') if dia else datetime.now()
        horarios_list = Agenda.objects.filter(dia=dia).order_by('status_atendimento', 'horario')
        paginator = Paginator(horarios_list, 2)
        page = request.GET.get('page')
        horarios = paginator.get_page(page)
        return render(request, 'horarios/agenda_list.html',
            {'horarios': horarios, 'data': datetime.strftime(dia, '%Y-%m-%d')})


class UpdateAgenda(UpdateView):
    model = Agenda
    template_name = 'horarios/agenda_form.html'
    form_class = AgendaForm
    success_url = reverse_lazy('list-agenda')


class DeleteAgenda(DeleteView):
    model = Agenda
    success_url = reverse_lazy('list-agenda')

from datetime import date, datetime
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from horarios.models import Agenda
from .forms import AgendaForm
# Create your views here.


class CreateAgenda(CreateView):
    def get(self, request):
        form = AgendaForm()
        return render(request, 'horarios/agenda_form.html',
            {'form': form})

    def post(self, request):
        Agenda.objects.create(
            dia=request.POST['dia'], horario=request.POST['horario'],
            cliente_id=request.POST['cliente']
        )
        return redirect(reverse_lazy('list-agenda'))


class ListAgenda(ListView):
    model = Agenda
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        data_busca = request.GET.get('data_busca', None)
        if data_busca:
            data_busca = datetime.strptime(data_busca, '%Y-%m-%d')
        else:
            data_busca = datetime.now()
        horarios_list = Agenda.objects.filter(dia=data_busca).order_by('horario')
        paginator = Paginator(horarios_list, 8)
        page = request.GET.get('page')
        horarios = paginator.get_page(page)
        return render(request, 'horarios/agenda_list.html',
            {'horarios': horarios, 'data': datetime.strftime(data_busca, '%Y-%m-%d')})


class UpdateAgenda(View):
    def get(self, request, pk):
        agenda = Agenda.objects.get(id=pk)
        form = AgendaForm(instance=agenda)
        return render(request, 'horarios/agenda_form.html', {'form': form})
    
    def post(self, request, pk):
        agenda = Agenda.objects.get(id=pk)
        agenda.dia = request.POST['dia']
        agenda.horario = request.POST['horario']
        agenda.cliente_id = request.POST['cliente']
        agenda.save()
        return redirect(reverse_lazy('list-agenda'))
from typing import List
from django.urls import reverse_lazy
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, ListView, UpdateView, View

from clientes.models import Cliente
from clientes.forms import ClienteForm


class CreateCliente(CreateView):
    def get(self, request):
        form = ClienteForm()
        return render(request, 'clientes/cliente_form.html',
            {'form': form})

    def post(self, request):
        Cliente.objects.create(
            nome=request.POST['nome'], data_nascimento=request.POST['data_nascimento'],
            telefone=request.POST['telefone'], endereco=request.POST['endereco']
        )
        return redirect(reverse_lazy('list-cliente'))


class ListCliente(ListView):
    model = Cliente
    paginate_by = 10


class UpdateCliente(View):
    def get(self, request, pk):
        cliente = Cliente.objects.get(id=pk)
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/cliente_form.html', {'form': form})
    
    def post(self, request, pk):
        cliente = Cliente.objects.get(id=pk)
        cliente.nome = request.POST['nome']
        cliente.data_nasc = request.POST['data_nascimento']
        cliente.telefone = request.POST['telefone']
        cliente.endereco = request.POST['endereco']
        cliente.save()
        return redirect(reverse_lazy('list-cliente'))

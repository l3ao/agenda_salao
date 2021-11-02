from django.db import models
from clientes.models import Cliente


# Create your models here.
class Agenda(models.Model):
    dia = models.DateField(verbose_name='Dia')
    horario = models.TimeField(verbose_name='Horário')
    cliente = models.ForeignKey(to=Cliente, on_delete=models.CASCADE)
    status_atendimento = models.BooleanField(
        verbose_name='Cliente atendida',
        default=False
    )

    class Meta:
        unique_together = [['dia', 'horario']]

from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(verbose_name='Nome completo', max_length=50)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    endereco = models.CharField(verbose_name='Endereço', max_length=100)
    telefone = models.CharField(verbose_name='Telefone', max_length=12)

    def __str__(self):
        return self.nome
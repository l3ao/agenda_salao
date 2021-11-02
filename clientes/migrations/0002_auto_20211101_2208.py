# Generated by Django 3.2.8 on 2021-11-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefone'),
        ),
    ]
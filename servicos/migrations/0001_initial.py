# Generated by Django 3.0 on 2019-12-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(blank=True, null=True)),
                ('servico', models.CharField(max_length=200, verbose_name='Descrição do Serviço')),
                ('tipo', models.CharField(max_length=10, verbose_name='Tipo do Pet')),
                ('tamanho', models.CharField(max_length=10, verbose_name='Tamanho do Pet')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor do Serviço')),
                ('ativo', models.BooleanField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('cadastro', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviço',
                'ordering': ['servico'],
            },
        ),
    ]

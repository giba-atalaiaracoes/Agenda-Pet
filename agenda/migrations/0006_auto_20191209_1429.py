# Generated by Django 3.0 on 2019-12-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_tamanhos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='tamanho',
            field=models.CharField(max_length=10, verbose_name='Tamanho do Pet'),
        ),
    ]
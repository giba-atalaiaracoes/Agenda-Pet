# Generated by Django 3.0 on 2019-12-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20191209_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='id_tutor',
        ),
        migrations.AddField(
            model_name='pet',
            name='tutor',
            field=models.CharField(default=1, max_length=200, verbose_name='Nome do Tutor'),
            preserve_default=False,
        ),
    ]

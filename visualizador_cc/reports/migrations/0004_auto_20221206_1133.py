# Generated by Django 3.2.12 on 2022-12-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_repcargosadultosformprof_repcargosadultosprimaria_repcargosadultossecundaria_repcargoscomunartistica'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='rephorasadultosformprof',
            table='rep_horas_adultos_form_prof',
        ),
        migrations.AlterModelTable(
            name='rephorasespecial',
            table='rep_horas_especial',
        ),
        migrations.AlterModelTable(
            name='rephorasinicialjardin',
            table='rep_horas_comun_inicial_jardin',
        ),
        migrations.AlterModelTable(
            name='rephorasinicialmaternal',
            table='rep_horas_comun_inicial_maternal',
        ),
    ]

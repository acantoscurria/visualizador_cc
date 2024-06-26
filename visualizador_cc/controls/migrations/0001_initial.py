# Generated by Django 3.2.12 on 2022-04-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConMatricComunInicial',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo_ed', models.TextField(blank=True, null=True)),
                ('nivel', models.TextField(blank=True, null=True)),
                ('cueanexo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_fila', models.IntegerField(blank=True, null=True)),
                ('escuela', models.CharField(blank=True, max_length=255, null=True)),
                ('sala', models.CharField(blank=True, max_length=255, null=True)),
                ('turno', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_secc', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_secc', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('total_var', models.IntegerField(blank=True, null=True)),
                ('menos_1_anio', models.IntegerField(blank=True, null=True)),
                ('un_anio', models.IntegerField(blank=True, null=True)),
                ('dos_anios', models.IntegerField(blank=True, null=True)),
                ('tres_anios', models.IntegerField(blank=True, null=True)),
                ('cuatro_anios', models.IntegerField(blank=True, null=True)),
                ('cinco_anios', models.IntegerField(blank=True, null=True)),
                ('seis_anios', models.IntegerField(blank=True, null=True)),
                ('total_disc', models.IntegerField(blank=True, null=True)),
                ('var_disc', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ConMatriculasComunInicial',
                'db_table': 'con_matric_comun_inicial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConMatricComunPrimaria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo_ed', models.TextField(blank=True, null=True)),
                ('nivel', models.TextField(blank=True, null=True)),
                ('cueanexo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_fila', models.IntegerField(blank=True, null=True)),
                ('escuela', models.CharField(blank=True, max_length=255, null=True)),
                ('turno', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre_secc', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_secc', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('total_var', models.IntegerField(blank=True, null=True)),
                ('nivel_or', models.CharField(blank=True, max_length=255, null=True)),
                ('grado_anio', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_5', models.IntegerField(blank=True, null=True)),
                ('edad_6', models.IntegerField(blank=True, null=True)),
                ('edad_7', models.IntegerField(blank=True, null=True)),
                ('edad_8', models.IntegerField(blank=True, null=True)),
                ('edad_9', models.IntegerField(blank=True, null=True)),
                ('edad_10', models.IntegerField(blank=True, null=True)),
                ('edad_11', models.IntegerField(blank=True, null=True)),
                ('edad_12', models.IntegerField(blank=True, null=True)),
                ('edad_13', models.IntegerField(blank=True, null=True)),
                ('edad_14', models.IntegerField(blank=True, null=True)),
                ('edad_15', models.IntegerField(blank=True, null=True)),
                ('edad_16', models.IntegerField(blank=True, null=True)),
                ('edad_17', models.IntegerField(blank=True, null=True)),
                ('edad_18_y_mas', models.IntegerField(blank=True, null=True)),
                ('total_rep', models.IntegerField(blank=True, null=True)),
                ('tot_alum_promoasis', models.IntegerField(blank=True, null=True)),
                ('var_alum_promoasis', models.IntegerField(blank=True, null=True)),
                ('tot_discapacidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ConMatriculasComunPrimaria',
                'db_table': 'con_matric_comun_primaria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConMatricComunSecundaria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo_ed', models.TextField(blank=True, null=True)),
                ('nivel', models.TextField(blank=True, null=True)),
                ('cueanexo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_fila', models.IntegerField(blank=True, null=True)),
                ('escuela', models.CharField(blank=True, max_length=255, null=True)),
                ('turno', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('total_var', models.IntegerField(blank=True, null=True)),
                ('nivel_or', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_12', models.IntegerField(blank=True, null=True)),
                ('edad_13', models.IntegerField(blank=True, null=True)),
                ('edad_14', models.IntegerField(blank=True, null=True)),
                ('edad_15', models.IntegerField(blank=True, null=True)),
                ('edad_16', models.IntegerField(blank=True, null=True)),
                ('edad_17', models.IntegerField(blank=True, null=True)),
                ('total_rep', models.IntegerField(blank=True, null=True)),
                ('var_rep', models.IntegerField(blank=True, null=True)),
                ('nro_orden_pe', models.IntegerField(blank=True, null=True)),
                ('anio_est', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_div', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_div', models.CharField(blank=True, max_length=255, null=True)),
                ('orientacion', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_11_y_menos', models.IntegerField(blank=True, null=True)),
                ('edad_18', models.IntegerField(blank=True, null=True)),
                ('edad_19', models.IntegerField(blank=True, null=True)),
                ('edad_25_y_mas', models.IntegerField(blank=True, null=True)),
                ('edad_20_24', models.IntegerField(blank=True, null=True)),
                ('denom_pe', models.CharField(blank=True, max_length=255, null=True)),
                ('total_disc', models.IntegerField(blank=True, null=True)),
                ('var_disc', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ConMatriculasComunSecundaria',
                'db_table': 'con_matric_comun_secundaria',
                'managed': False,
            },
        ),
    ]

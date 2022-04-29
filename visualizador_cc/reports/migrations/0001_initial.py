# Generated by Django 3.2.12 on 2022-04-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepMatricComunInicial',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
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
                ('nom_est', models.CharField(blank=True, max_length=255, null=True)),
                ('nro_est', models.CharField(blank=True, max_length=255, null=True)),
                ('anio_creac_establec', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creac_establec', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('udt', models.CharField(blank=True, max_length=255, null=True)),
                ('cui', models.CharField(blank=True, max_length=255, null=True)),
                ('cua', models.CharField(blank=True, max_length=255, null=True)),
                ('cuof', models.CharField(blank=True, max_length=255, null=True)),
                ('sector', models.CharField(blank=True, max_length=255, null=True)),
                ('ambito', models.CharField(blank=True, max_length=255, null=True)),
                ('ref_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('calle', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=255, null=True)),
                ('localidad', models.CharField(blank=True, max_length=255, null=True)),
                ('departamento', models.CharField(blank=True, max_length=255, null=True)),
                ('cod_postal', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_est', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_cod_area', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_nro', models.CharField(blank=True, max_length=255, null=True)),
                ('per_funcionamiento', models.CharField(blank=True, max_length=255, null=True)),
                ('email_loc', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'rep_matric_comun_inicial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RepMatricComunPrimaria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cueanexo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_fila', models.IntegerField(blank=True, null=True)),
                ('escuela', models.CharField(blank=True, max_length=255, null=True)),
                ('turno', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre_secc', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_secc', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('total_var', models.IntegerField(blank=True, null=True)),
                ('nivel', models.CharField(blank=True, max_length=255, null=True)),
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
                ('var_rep', models.IntegerField(blank=True, null=True)),
                ('tot_alum_promoasis', models.IntegerField(blank=True, null=True)),
                ('var_alum_promoasis', models.IntegerField(blank=True, null=True)),
                ('tot_discapacidad', models.IntegerField(blank=True, null=True)),
                ('var_discapacidad', models.IntegerField(blank=True, null=True)),
                ('nom_est', models.CharField(blank=True, max_length=255, null=True)),
                ('nro_est', models.CharField(blank=True, max_length=255, null=True)),
                ('anio_creac_establec', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creac_establec', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('udt', models.CharField(blank=True, max_length=255, null=True)),
                ('cui', models.CharField(blank=True, max_length=255, null=True)),
                ('cua', models.CharField(blank=True, max_length=255, null=True)),
                ('cuof', models.CharField(blank=True, max_length=255, null=True)),
                ('sector', models.CharField(blank=True, max_length=255, null=True)),
                ('ambito', models.CharField(blank=True, max_length=255, null=True)),
                ('ref_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('calle', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=255, null=True)),
                ('localidad', models.CharField(blank=True, max_length=255, null=True)),
                ('departamento', models.CharField(blank=True, max_length=255, null=True)),
                ('cod_postal', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_est', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_cod_area', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_nro', models.CharField(blank=True, max_length=255, null=True)),
                ('per_funcionamiento', models.CharField(blank=True, max_length=255, null=True)),
                ('email_loc', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'rep_matric_comun_primaria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RepMatricComunSecundaria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cueanexo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_fila', models.IntegerField(blank=True, null=True)),
                ('turno', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('total_var', models.IntegerField(blank=True, null=True)),
                ('nivel', models.CharField(blank=True, max_length=255, null=True)),
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
                ('nom_est', models.CharField(blank=True, max_length=255, null=True)),
                ('nro_est', models.CharField(blank=True, max_length=255, null=True)),
                ('anio_creac_establec', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creac_establec', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('udt', models.CharField(blank=True, max_length=255, null=True)),
                ('cui', models.CharField(blank=True, max_length=255, null=True)),
                ('cua', models.CharField(blank=True, max_length=255, null=True)),
                ('cuof', models.CharField(blank=True, max_length=255, null=True)),
                ('sector', models.CharField(blank=True, max_length=255, null=True)),
                ('ambito', models.CharField(blank=True, max_length=255, null=True)),
                ('ref_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('calle', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=255, null=True)),
                ('localidad', models.CharField(blank=True, max_length=255, null=True)),
                ('departamento', models.CharField(blank=True, max_length=255, null=True)),
                ('cod_postal', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_est', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_cod_area', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono_nro', models.CharField(blank=True, max_length=255, null=True)),
                ('per_funcionamiento', models.CharField(blank=True, max_length=255, null=True)),
                ('email_loc', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'rep_matric_comun_secundaria',
                'managed': False,
            },
        ),
    ]

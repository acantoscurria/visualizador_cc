# Generated by Django 3.2.12 on 2022-05-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepMatricComunSnu',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cueanexo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_fila', models.IntegerField(blank=True, null=True)),
                ('escuela', models.CharField(blank=True, max_length=255, null=True)),
                ('n_plan_estudio', models.CharField(blank=True, max_length=255, null=True)),
                ('plan_est_titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_carrera', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_formacion', models.CharField(blank=True, max_length=255, null=True)),
                ('modalidad_dicatado', models.CharField(blank=True, max_length=255, null=True)),
                ('carrera_termino', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.CharField(blank=True, max_length=255, null=True)),
                ('total_var', models.CharField(blank=True, max_length=255, null=True)),
                ('menos_18_años', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_18', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_19', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_20', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_21', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_22', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_23', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_24', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_25', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_26', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_27', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_28', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_29', models.CharField(blank=True, max_length=255, null=True)),
                ('edad_30', models.CharField(blank=True, max_length=255, null=True)),
                ('total_ingresante', models.CharField(blank=True, max_length=255, null=True)),
                ('var_ingresante', models.CharField(blank=True, max_length=255, null=True)),
                ('total_pasantia_practicas', models.CharField(blank=True, max_length=255, null=True)),
                ('var_pasantia_practicas', models.CharField(blank=True, max_length=255, null=True)),
                ('total_residencia', models.CharField(blank=True, max_length=255, null=True)),
                ('var_residencia', models.CharField(blank=True, max_length=255, null=True)),
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
                'db_table': 'rep_matric_comun_snu',
                'managed': False,
            },
        ),
    ]
